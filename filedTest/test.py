import requests
import json
BASE_URL='http://127.0.0.1:8000/testapp/'
ENDPOINT='GET/'
fileType="song/"
def get_resources(id=None):
    data={}
    if id is not None:
        resp = requests.get(BASE_URL+ENDPOINT+fileType+str(id))
    else:
        resp = requests.get(BASE_URL+ENDPOINT+fileType)
    print(resp.status_code)
    if resp.status_code==200:
        print(resp.json())
get_resources(2)
get_resources(-2)
get_resources("sahil")
get_resources("../song")
get_resources("?id=3")
get_resources("?id!=3")
get_resources("?www.google.com")
get_resources("/www.google.com")

#I had tested CURD operations with postman
#I had also tested it with possible url injection payloads with burp suit