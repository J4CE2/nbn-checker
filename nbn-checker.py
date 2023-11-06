import json
import datetime
import sqlite3 as sl
import os
import sys
from enum import IntEnum

try:
    from urllib.request import Request, urlopen  # Python 3
except ImportError:
    from urllib2 import Request, urlopen  # Python 2


nbn_url = 'https://places.nbnco.net.au/places/v2/details/'
location_id = 'LOC000000000000'


#NBN connection / read JSON data
req = Request(nbn_url + location_id)
req.add_header('Referer', 'https://www.nbnco.com.au/')
content = urlopen(req).read()

#JSON file
jsondata = json.loads(content)

reasonCode = jsondata.get('addressDetail').get('reasonCode')
altReasonCode = jsondata.get('addressDetail').get('altReasonCode')
techChangeStatus = jsondata.get('addressDetail').get('techChangeStatus')
programType = jsondata.get('addressDetail').get('programType')
targetEligibilityQuarter = jsondata.get('addressDetail').get('targetEligibilityQuarter')
techType = jsondata.get('addressDetail').get('techType')
formattedAddress = jsondata.get('addressDetail').get('formattedAddress')

print("")
print("---------------------- SUMMARY -----------------")
print("Address: " + formattedAddress)
print("Current Technology: " + techType)
print("reasonCode: " + reasonCode)
print("altReasonCode: " + altReasonCode)
print("techChangeStatus: " + techChangeStatus)
print("programType: " + programType)
print("targetEligibilityQuarter: " + targetEligibilityQuarter)
print("")
print("---------------------- FULL DATA DUMP -----------------")

print(json.dumps(jsondata, indent=4))
