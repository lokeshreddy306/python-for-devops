from flask import Flask, jsonify, request
import requests
from requests.auth import HTTPBasicAuth
import json
import os

app = Flask(__name__)

@app.route("/createJira", methods=["POST"])
def createJira():
    github_payload = request.json

    url = "https://lokeshasi768.atlassian.net/rest/api/3/issue"

    token = os.getenv("API_TOKEN")
    
    auth = HTTPBasicAuth("lokeshasi768@gmail.com", token)


    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    issue_title = github_payload.get("issue",{}).get("title", "")
    payload = json.dumps ( {
        "fields": {
            "project": {
                "key": "PY"
            },
            "summary": issue_title,
            "issuetype": {
                "name": "Task"
            }
        },
        "update": {}
    } )

    comment = github_payload.get("comment",{}).get("body", "")
    
    if comment.strip() == "/createJira":
        response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )    
        print("Status:", response.status_code)
        print("Response:", response.text)
        return jsonify(response.json())
    else:
        return jsonify({"message":"the jira ticket is not created"})

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000)


