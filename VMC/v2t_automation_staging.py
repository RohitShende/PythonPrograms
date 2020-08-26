import requests
import time
import datetime

org_id = "ba6a3e3e-2cb5-45eb-bc73-b046c2545dcd"
sddc_id = "10ec4eff-28bb-4065-be34-d6f7a0e54fce"
refresh_token = "67651dab-2dee-43ad-8fb4-e9cdf29b3757"
csp_auth_token = ""

base_url = "https://stg-int.skyscraper.vmware.com"
sddc_url = "https://stg.skyscraper.vmware.com/vmc/api/orgs/"+org_id+"/sddcs/"+sddc_id
auth_url = "https://console-stg.cloud.vmware.com/csp/gateway/am/api/auth/api-tokens/authorize?refresh_token=" + \
           refresh_token

headers = {
    "Content-Type": "application/json"
}

csp_headers = headers



task_id = input('Enter task id:-')



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
    r = requests.post(auth_url, headers=headers)
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

            start_time = data['start_time']
            end_time = data['end_time']
            start_time = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S.%fZ")
            end_time = datetime.datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%S.%fZ")
            task_time = end_time - start_time
            print('Task Completed in :', task_time)

            print("\n>>>>> TASK FAILED <<<< \n")
            break

        elif task_status == "FINISHED" or task_sub_status == "FINISHED":
            print("\nTASK FINISHED SUCCESSFULLY !!!")
            start_time = data['start_time']
            end_time = data['end_time']
            start_time = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S.%fZ")
            end_time = datetime.datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%S.%fZ")
            task_time = end_time - start_time
            print('Task Completed in :', task_time)
            break

        else:
            print('Sleeping for 10 seconds .... ')
            time.sleep(10)


if __name__ == '__main__':
    print("********** STARTING V2T MIGRATION ***************\n")
    get_csp_auth_token()
    # get_sddc_details()
    poll_task_details(task_id)
    # print("\n********** V2T MIGRATION DONE SUCCESSFULLY ************")
