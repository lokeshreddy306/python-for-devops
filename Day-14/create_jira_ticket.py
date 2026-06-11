# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://lokeshasi768.atlassian.net/rest/api/3/issue"

token = os.getenv("API_TOKEN")
auth = HTTPBasicAuth("lokeshasi768@gmail.com", token)


headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "project": {
            "key": "PY"
        },
        "summary": "My first Jira ticket from Python",
        "issuetype": {
            "name": "Task"
        }
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.loads(response.text))