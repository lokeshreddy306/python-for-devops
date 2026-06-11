import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://lokeshasi768.atlassian.net/rest/api/3/project"

token = os.getenv("API_TOKEN")
auth = HTTPBasicAuth("lokeshasi768@gmail.com", token)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
    "key": "PY",
    "name": "Jiraautomation",
    "projectTypeKey": "business",
    "projectTemplateKey": "com.atlassian.jira-core-project-templates:jira-core-simplified-process-control",
    "leadAccountId": "712020:d0f8ebc7-5f25-44f9-bf0c-bbcaa605d103"
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.loads(response.text))