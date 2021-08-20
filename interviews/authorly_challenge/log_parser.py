# Output csv
# POST  ||      Status Code   ||  Response Size   || city_id  || change_latitude  ||  current_latitude   ||
# type   ||  newSearch || listType etc. (All columns in the above lines should be captured in the .csv Output file)

import re
import json
import pandas as pd

python_pattern = '(?P<datetime1>[\d]{2}-[\d]{2}-[\d]{4} [\d]{2}:[\d]{2}:[\d]{2} \+[\d]{2}:[\d]{2}): (header) - \"(?P<code>[\d]*)\" \[(?P<datetime>[^\]]+)\] POST (?P<request>[^ \"]+) (?P<body>\{.*\}) \"Status code :\"(?P<status>[0-9]{3})  \"Response Size :\"(?P<response_size>[\d]+) \"Response time :\" (?P<response_time>.* ms)'
print('Parsing for POST requests from nginx logs...')
with open('nginx_log.txt') as f:
    file_data = f.readlines()

compiled_pattern = re.compile(python_pattern)
count = 1
columns = ['POST', 'Status Code', 'Response Size', 'city_id', 'change_latitude', 'current_latitude', 'type',
           'newSearch', 'listType', 'response_time', 'datetime']

rows = []
for line in file_data:
    match = compiled_pattern.search(line)
    if match:
        d = match.groupdict()
        body = json.loads(d['body'])
        row = [d.get('request'), d.get('status'), d.get('response_size'), body.get('city_id'),
               body.get('change_latitude'), body.get('change_latitude'), body.get('type'), body.get('newSearch'),
               body.get('listType'), d.get('response_time'), d.get('datetime')]
        # print(row)
        rows.append(row)
        count += 1

df = pd.DataFrame(data=rows, columns=columns)
print(f'Found {df.shape[0]} POST records out of total {len(file_data)} lines nginx log')
output_file = 'output_parsed_post_api_data.csv'
df.to_csv(output_file, index=False)
print(f'Written the parsed data of {df.shape[0]} records to {output_file} Successfully !')
