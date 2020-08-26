# GET /api/4.0/edges/{edgeId}

import requests
from requests.auth import HTTPBasicAuth

vsmIp = '10.108.162.28'
username = 'admin'
password = 'default'
api = '/api/4.0/edges/'
component = 'edge-'

for i in range(240, 270):
    print('Deleting Edge - ' + str(i))
    res = requests.delete('https://' + vsmIp + ':443/' + api + component + str(i),
                          auth=HTTPBasicAuth(username, password), verify=False)
    print(res.status_code)

print('********* DONE ***********')