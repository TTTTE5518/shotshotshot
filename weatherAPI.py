import json
import urllib.request
import urllib.error
import urllib.parse
import ssl
import sys

def replaceSpaces(input):
    inject = "%20"
    for i in range(len(input)):
        if(input[i] == ' '):
            input = input.replace(input[i], inject)
            
    return input

# 忽略 SSL 憑證驗證（僅 for 測試）
ssl._create_default_https_context = ssl._create_unverified_context

BaseURL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

ApiKey = parent().par.Apikey.eval()
UnitGroup='us'

Location = replaceSpaces(parent().par.Location.eval())

StartDate = ''
EndDate=''
ContentType="json"
Include="current"

ApiQuery = BaseURL + urllib.parse.quote(Location)

if (len(StartDate)):
    ApiQuery+="/"+StartDate
    if (len(EndDate)):
        ApiQuery+="/"+EndDate

ApiQuery+="?"

params = []
if (len(UnitGroup)):
    params.append("unitGroup="+UnitGroup)
if (len(ContentType)):
    params.append("contentType="+ContentType)
if (len(Include)):
    params.append("include="+Include)
params.append("key="+ApiKey)

ApiQuery += "&".join(params)

print(' - Running query URL: ', ApiQuery)
print()

try:
    data = urllib.request.urlopen(ApiQuery)
except urllib.error.HTTPError as e:
    ErrorInfo= e.read().decode()
    print('Error code: ', e.code, ErrorInfo)
    sys.exit()
except urllib.error.URLError as e:
    print('Error reason:', e.reason)
    sys.exit()

weatherData = json.loads(data.read().decode('utf-8'))

# 若 TouchDesigner:
op('request_output').text = json.dumps(weatherData)


