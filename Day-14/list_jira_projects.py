import requests
from requests.auth import HTTPBasicAuth
import json
import os


url = "https://lokeshasi768.atlassian.net/rest/api/3/project"

token = os.getenv("API_TOKEN")
auth = HTTPBasicAuth("lokeshasi768@gmail.com", token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

my_jira_project_data = json.loads(response.text)

print(my_jira_project_data)