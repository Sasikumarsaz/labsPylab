import requests
import json
response = requests.get("https://10.64.40.48:9070/api/tm/8.5/config/active/virtual_servers", auth=("admin", "password123"), verify=False) ## API get request using auth and verify is to ignore cert
print(response.status_code)  # To get the response code
print(json.dumps(response.json(), indent=4)) # It will print the response outcome in json format
