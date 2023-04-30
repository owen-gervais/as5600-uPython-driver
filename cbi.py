import requests

# Grab the prefix
cbi_url = "https://api.community-boating.org/api/flag"
preFix = "var FLAG_COLOR = \""
postFix = "\""

# Dictionary of user responses
responses = {"C":"CBI is Closed", "G":"CBI is at Green Flag", "Y":"CBI is at Yellow Flag", "R":"CBI is at Red Flag"}

resp = requests.get(cbi_url)

print("Raw response: {}".format(resp.content))

decodedContent = resp.content.decode("utf-8")

status = decodedContent.replace(preFix, "").replace(postFix, "")

print(responses[status])