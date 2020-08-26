import jenkins
import pprint

staging_jenkins_url = 'https://nsxqe-jenkins-stage.svc.eng.vmware.com/'
production_jenkins_url = 'https://nsxqe-jenkins.svc.eng.vmware.com/'

JENKINS_UN = 'svc.nsxqe-cibot'
JENKINS_API_TOKEN = '111ddde4d44ef999915bbab5a25ac9063d'

all_jenkins_jobs = {}

server = jenkins.Jenkins(staging_jenkins_url, username=JENKINS_UN, password=JENKINS_API_TOKEN)
print(server.jobs_count())

branch = 'nsx-grindcore'
pipeline = 'gating'
area = 'Edge-L4-L7'
suite = 'DHCP_LEASE_DELETE.BAT'
build = '16019387'

job_name = '{}-{}-{}-job-scm'.format(branch, pipeline, area)
job_name = 'nsx-grindcore-bat-Edge-L4-L7-job-scm'

print('\n======================================\n')
# build a parameterized job
# requires creating and configuring the api-test job to accept 'param1' & 'param2'

# pprint.pprint(server.get_job_info(job_name))


# last_build_number = server.get_job_info(job_name)['lastCompletedBuild']['number']
# build_info = server.get_build_info(job_name, last_build_number)
# pprint.pprint(build_info)

# 'FRAMEWORK_BRANCH': 'rtqa-staging', 'ESX_BUILD_NUMBER', 'VC_BUILD_NUMBER', 'PACE_BUILD_NUMBER'

server.build_job(job_name, parameters={'NSX_BUILD_NUMBER': build, 'RUN_SPECIFIC_SUITES': suite})

print('Suite triggered successfully')