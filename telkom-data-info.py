# DESCRIPTION: This script is for fetching balances for the current sim-card on telkom
#              The amount of data, airtime, and voice bundles left and when they expire
# 
# REQUIREMENT: requests


from requests.sessions import Session

session = Session()

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.58 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Sec-GPC': '1',
    'Origin': 'https://onnetsecure.telkom.co.za',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Language': 'en-ZA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
}

response = session.get('https://onnetsecure.telkom.co.za/onnet/public/mobileData', headers=headers)

cellphone = response.text.split('id="mobileNumber" value="', 1)[1][0:10]

data = {
    'callCount' : '1',
    'scriptSessionId' : '',
    'c0-scriptName' : 'mobileDataServiceWrapper',
    'c0-methodName' : 'getFreeResources',
    'c0-id' : '0',
    'c0-param0' : 'string:'+cellphone,
    'batchId' : '2'
}

response = session.post('https://onnetsecure.telkom.co.za/onnet/public/dwr/call/plaincall/mobileDataServiceWrapper.getFreeResources.dwr', headers=headers, data=data)
# response = response.text.split("\n",3)[3] # remove the first 3 lines, they are useless
print(response)