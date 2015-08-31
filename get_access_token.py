import requests
import base64

key = "your key"
secret = "your-secret"
bearer_token = base64.b64encode(key+":"+secret)
url = "https://api.twitter.com/oauth2/token"
headers = {"Authorization": "Basic "+bearer_token,"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}
data = "grant_type=client_credentials"
r = requests.post(url,headers=headers,data=data)
access_token = r.json()["access_token"]
print "access", access_token