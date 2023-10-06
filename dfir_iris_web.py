# !/usr/bin/env python

import sys
import json
import requests
from requests.auth import HTTPBasicAuth

# Read configuration parameters
alert_file = open(sys.argv[1])
# user = sys.argv[2].split(':')[0]
# api_key = sys.argv[2].split(':')[1]
hook_url = sys.argv[3]
# Read the alert file
alert_json = json.loads(alert_file.read())
alert_file.close()

# Extract issue fields
alertlevel = alert_json['rule']['level']
ruleid = alert_json['rule']['id']
ruledescription = alert_json['rule']['description']
agentid = alert_json['agent']['id']
agentname = alert_json['agent']['name']
fullog = alert_json['full_log']

# Set the project attributes ===> This section needs to be manually configured before running!
# statusid = 'Active'     # You can get this from the beggining of an issue key. For example, WS for issue key WS-5018
# visibility = 'Open'  # Check https://confluence.atlassian.com/jirakb/finding-the-id-for-issue-types-646186508.html. There's also an API endpoint to get it.
# authToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTY0ODM1NTAuMjU4Njc4LCJlbWFpbCI6Im5hdmlua3I0MzFAZ21haWwuY29tIn0.h4T_PPK2r2HQ6oTvEG2y8x8DWyWwwMHDiCCGauaehVY'
# Generate request
# headers = {'content-type': 'application/json'}
headers = {
    'Authorization': 'Bearer B8BA5D730210B50F41C06941582D7965D57319D5685440587F98DFDC45A01594',
    'Content-Type': 'application/json'
}

issue_data = {

        "alert_title": 'WAZUH alert on ' + agentname + '',
        "alert_status_id":"1",
        "alert_customer_id":"1",
        "alert_severity_id":"1",
        "alert_description": ' Details: ' + ruledescription + ' "\n" Agenid: '+ agentid + ' "\n" Agentname: ' + agentname + ' "\n" Ruleid: ' + ruleid + ' "\n" Fullog: ' + fullog + ' '

}

# Send the request
response = requests.post(hook_url, data=json.dumps(issue_data), headers=headers)
#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4,
#                 separators=(",", ": ")))  # <--- Uncomment this line for debugging

sys.exit(0)
