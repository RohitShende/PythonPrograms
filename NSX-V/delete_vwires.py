import requests
from requests.auth import HTTPBasicAuth

vsmIp = '10.108.162.28'
username = 'admin'
password = 'default'
api = 'api/2.0/vdn/virtualwires/'
component = 'virtualwire-'

for i in range(1141, 1146):
    print('Deleting Virtual Wire - ' + str(i))
    res = requests.delete('https://' + vsmIp + ':443/' + api + component + str(i),
                          auth=HTTPBasicAuth(username, password), verify=False)
    print(res.status_code)

print('********* DONE ***********')