import requests
from request_boost import boosted_requests

# Config
number_of_sample_urls = 100

# Sample data
urls = [f'https://postman-echo.com/get?random_data={test_no}' for test_no in range(number_of_sample_urls)]
post_urls = [f'https://postman-echo.com/post' for test_no in range(number_of_sample_urls)]
headers = [{'sample_header': test_no} for test_no in range(number_of_sample_urls)]
data = [{'sample_data': test_no} for test_no in range(number_of_sample_urls)] # Required for POST requests,
#For POST request data can be just list of empty dict but not NONE


headers = [
    {'Content-Type': 'application\\json', 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJub25jZSI6IlRMZG1KTmU1UVhnX1A3OVNtOTVubldzT1B5TDA1U1VxT09vaHZVbDZ3dGciLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9mYWJiNjFiOC0zYWZlLTRlNzUtYjkzNC1hNDdmNzgyYjhjZDcvIiwiaWF0IjoxNjg5MzIzMzIzLCJuYmYiOjE2ODkzMjMzMjMsImV4cCI6MTY4OTMyODY2NiwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhUQUFBQTJGVWVUclpib2pnRTJTNm1kZ3V6ako2dkh4MXJpMmpmZUlaWFVBa3R4MUl0RWl5VUpINEtJSG5rbm5hYnRIbkJwczlqeThJOHNJRlUvWTZWdTNVclUwM2xkZHh5SWd3eEFhZkNKSHFsTm1BPSIsImFtciI6WyJwd2QiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiTWljcm9zb2Z0IEF6dXJlIENMSSIsImFwcGlkIjoiMDRiMDc3OTUtOGRkYi00NjFhLWJiZWUtMDJmOWUxYmY3YjQ2IiwiYXBwaWRhY3IiOiIwIiwiZGV2aWNlaWQiOiI5MjE4MWU3OC1kN2JlLTQ4MWUtODM3Ni1lOGI5YTU4MDMyMzgiLCJmYW1pbHlfbmFtZSI6IlZlbXVyaSIsImdpdmVuX25hbWUiOiJBamF5IEt1bWFyIiwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiMjYwMToyYzY6NDM4MTpkZTYwOjRkZmI6YWE0YTpmMzM4OjJhNCIsIm5hbWUiOiJWZW11cmksIEFqYXlLdW1hciAoQ29udHJhY3RvcikiLCJvaWQiOiJlZjU0MzJkZC1kZmQ1LTQyNTgtYjlmZC1hMGQwNzU4NTdmMzAiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMjEzMDUyMjQ3OC0xNzI1MTg4MDk0LTc4NjQ5ODYyNy03MTU0NTIiLCJwbGF0ZiI6IjUiLCJwdWlkIjoiMTAwMzIwMDJBNUNFRUQzQiIsInJoIjoiMC5BUk1BdUdHNy12NDZkVTY1TktSX2VDdU0xd01BQUFBQUFBQUF3QUFBQUFBQUFBQVRBTDQuIiwic2NwIjoiQXVkaXRMb2cuUmVhZC5BbGwgRGlyZWN0b3J5LkFjY2Vzc0FzVXNlci5BbGwgZW1haWwgR3JvdXAuUmVhZFdyaXRlLkFsbCBvcGVuaWQgcHJvZmlsZSBVc2VyLlJlYWRXcml0ZS5BbGwiLCJzaWduaW5fc3RhdGUiOlsiZHZjX21uZ2QiLCJkdmNfY21wIiwia21zaSJdLCJzdWIiOiJzeXQ3elhWS1EyVDZmN3I2Nm5xSWZLZFZOTTZQSXluMk9HdEE3MksxTGhvIiwidGVuYW50X3JlZ2lvbl9zY29wZSI6Ik5BIiwidGlkIjoiZmFiYjYxYjgtM2FmZS00ZTc1LWI5MzQtYTQ3Zjc4MmI4Y2Q3IiwidW5pcXVlX25hbWUiOiJBamF5S3VtYXIuVmVtdXJpQENWU0hlYWx0aC5jb20iLCJ1cG4iOiJBamF5S3VtYXIuVmVtdXJpQENWU0hlYWx0aC5jb20iLCJ1dGkiOiIwZXNKS1NtR1AwMnpKWWhfNk45Y0FBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJmMmVmOTkyYy0zYWZiLTQ2YjktYjdjZi1hMTI2ZWU3NGM0NTEiLCJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NjIjpbIkNQMSJdLCJ4bXNfc3QiOnsic3ViIjoiVkZ5MnNtMldvdmxKWkFXbEY2RlZnUHhPTjFVcDdzM3NDa0RYVVRaWmxvMCJ9LCJ4bXNfdGNkdCI6MTM4NjM0ODg0Nn0.jfUzbMy8CIxN_uJt3IuPYY_i6ZsUuWWH6THTioMho2neFuOigYCH6CBnUzsMRnNe9k5WRa87vj6-uPemBsb0a7rTKpuT_p6kX1Q-6g8VPtn-HRguPvbEQahAMtOWTjzWtJWl4m8v4qfKkANsz2ZmZ1BYYLD0ZsDaUqFHUe54_DNhndDhFL3UBA35LMi-m1-VEAzERw4DZKyxVZkqhDx_hYtzHziU0jWsyvGCIuBInFo6WVy4q1_m68Z0_k-fH1VqUHXFqyUaVGan31kCFZBLsb5SP71NOQN3uiGh63nHOTzD_T0oQVk7Gn9uwIUBvMa-mFU_tlNdD5lCWyAEB2CBmg', 'ConsistencyLevel': 'eventual'}
] * 3

urls = ['https://graph.microsoft.com/v1.0/servicePrincipals/1424e565-9f8f-476c-836a-ed3ea2ca3a7f', 'https://graph.microsoft.com/v1.0/servicePrincipals/70ed441c-5f5a-4cf1-8b23-aec5b50749eb', 'https://graph.microsoft.com/v1.0/servicePrincipals/9fdc0227-8741-4048-ab65-6c06c3a59972']
        # 'https://graph.microsoft.com/v1.0/servicePrincipals/a219b8fe-cd98-4793-b8e4-f94561a51b40', 'https://graph.microsoft.com/v1.0/servicePrincipals/a219b8fe-cd98-4793-b8e4-f94561a51b40', 'https://graph.microsoft.com/v1.0/servicePrincipals/4ffb5e9d-3a5b-41a3-96f9-aea3f5d76bbf', 'https://graph.microsoft.com/v1.0/servicePrincipals/0f007f60-be6a-4f74-abd7-469faa9c2868', 'https://graph.microsoft.com/v1.0/servicePrincipals/a219b8fe-cd98-4793-b8e4-f94561a51b40', 'https://graph.microsoft.com/v1.0/servicePrincipals/9fdc0227-8741-4048-ab65-6c06c3a59972', 'https://graph.microsoft.com/v1.0/servicePrincipals/723e60de-6f0f-4695-9717-1a6855469b6e', 'https://graph.microsoft.com/v1.0/servicePrincipals/9fdc0227-8741-4048-ab65-6c06c3a59972']

# results = boosted_requests(urls=urls, no_workers=16, max_tries=5, timeout=5, headers=None, verbose=False, parse_json=True)
results = boosted_requests(urls=urls, no_workers=16, max_tries=1, timeout=5, headers=headers, verbose=False)
# results = boosted_requests(urls=post_urls, no_workers=16, max_tries=5, timeout=5, headers=headers, data=data, verbose=True, parse_json=True)

print(*[i['displayName'] if i else None for i in results], sep="\n")


# test code
resp = requests.get(urls[0], headers=headers[0])
print(resp.status_code)
