import requests
import time

org_id = "8eff6f8d-ed7d-473b-be29-5ba868284c35"
sddc_id = "7cba6cbd-b8c6-4357-99cb-f73f0f8bd70c"
refresh_token = "6096eadd-eaf8-47b7-8eb6-632d7406e250"
csp_auth_token = ""

base_url = "https://internal.vmc.vmware.com"  # "https://stg-int.skyscraper.vmware.com"
sddc_url = "https://internal.vmc.vmware.com/vmc/api/orgs/" + org_id + "/sddcs/" + sddc_id
auth_url = "https://console.cloud.vmware.com/csp/gateway/am/api/auth/api-tokens/authorize"
headers = {
    "Content-Type": "application/json"
}

csp_headers = headers

task_id = input('Enter the Task ID-')


# Steps = [
#
#     ('POST' , '/vmc/api/orgs/'+org_id+'/sddcs/'+sddc_id+'/migration?action=prepare'),
#     ('POST' , '/vmc/api/orgs/'+org_id+'/sddcs/'+sddc_id+'/networking/migration/stages/prepare?mode=migration'),
#     ('POST', '/vmc/api/orgs/'+org_id+'/sddcs/'+sddc_id+'/networking/migration/stages/precheck?action=start'),
#
#
# Get Feedback: /vmc/api/orgs/{orgId}/sddcs/{sddcId}/networking/migration/feedback
#
# Post Feedback: /vmc/api/orgs/{orgId}/sddcs/{sddcId}/networking/migration/feedback
#
# POST /vmc/api/orgs/{orgId}/sddcs/{sddcId}/networking/migration/stages/precheck?action=continue
#
# Logical Constructs
#
# POST /vmc/api/orgs/{orgId}/sddcs/{sddcId}/networking/migration/stages/logicalconstructs?action=continue
#
# Edge Cutover
#
# POST /vmc/api/orgs/{orgId}/sddcs/{sddcId}/networking/migration/stages/edge?action=continue
# Infra Migration
#
# POST /vmc/api/orgs/{orgId}/sddcs/{sddcId}/networking/migration/stages/infrastructure?action=continue
# ]

def get_csp_auth_token():
    global csp_auth_token, csp_headers
    print("\n-->Calling get_csp_auth_token")
    print("POST ", auth_url)
    body = {
        "refresh_token": refresh_token
    }

    r = requests.post(auth_url, headers={"Content-Type": "application/x-www-form-urlencoded"}, data=body)
    status = r.status_code

    r.raise_for_status()

    data = r.json()

    print("Response Code :", status)
    print("Response Text :", data)

    new_csp_auth_token = data["access_token"]

    csp_auth_token = new_csp_auth_token

    csp_headers["csp-auth-token"] = csp_auth_token

    print("csp-auth-token changed to : ", csp_auth_token)


def get_sddc_details():
    print("\n--> Calling get_sddc_details")
    print("GET ", sddc_url)

    r = requests.get(sddc_url, headers=csp_headers)
    status = r.status_code
    if status == 401:
        get_csp_auth_token()
        r = requests.get(sddc_url, headers=csp_headers)

    r.raise_for_status()

    data = r.json()

    print("Response Code :", status)
    print("Response Text :", data)

    print('\nSDDC_NAME :', data["name"])
    print("SDDC_STATE :", data["sddc_state"])
    print("GLCM_BUNDLE", data["resource_config"]["sddc_manifest"]["glcm_bundle"])
    print("Number of Hosts : ", len(data["resource_config"]["esx_hosts"]))

    if data["resource_config"]["sddc_manifest"]["glcm_bundle"]["id"] == "":
        raise Exception("ERROR in Deployment - GLCM Bundle ID = ''")

    else:
        print("SDDC is Ready for V2T Migration")


def poll_task_details(task_id):
    print('\n-->Calling Poll Task Details...')
    url = base_url + '/vmc/skynet/api/orgs/' + org_id + '/tasks/' + task_id

    while True:
        print("\nCalling GET ", url)
        r = requests.get(url, headers=csp_headers)
        if r.status_code == 401:
            get_csp_auth_token()
            r = requests.get(url, headers=csp_headers)

        r.raise_for_status()
        data = r.json()
        print("Response Code :", r.status_code)
        task_status = data["status"]
        task_sub_status = data["sub_status"]

        print("TASK_STATUS - {} \nTASK_SUB_STATUS - {}".format(task_status, task_sub_status))
        if data.get("progress_percent"):
            print("PROGRESS PERCENTAGE - {}".format(data["progress_percent"]))
        if data.get("estimated_remaining_minutes"):
            print("ESTIMATED REMAINING TIME - {}".format(data["estimated_remaining_minutes"]))

        if task_status == "FAILED" or task_sub_status == "FAILED":
            task_error_message = data['error_message']
            print("\nTASK_ERROR_MESSAGE - {}".format(task_error_message))
            if data.get("params"):
                if data["params"].get("overall_status"):
                    task_overall_status = data["params"]["overall_status"]
                    print("TASK_OVERALL_STATUS - {}".format(task_overall_status))
                if data["params"].get("cleanup_result"):
                    cleanup_result = data["params"]["cleanup_result"]
                    print("TASK_CLEANUP_RESULT - {}".format(cleanup_result))

            print("\n>>>>> TASK FAILED <<<< \n")
            break

        elif task_status == "FINISHED" or task_sub_status == "FINISHED":
            print("\nTASK FINISHED SUCCESSFULLY !!!")
            break

        else:
            print('Sleeping for 10 seconds .... ')
            time.sleep(10)


if __name__ == '__main__':
    print("********** STARTING V2T MIGRATION ***************\n")
    get_csp_auth_token()
    # get_sddc_details()
    poll_task_details(task_id)
    print("\n********** V2T MIGRATION DONE SUCCESSFULLY ************")
