import os
import urllib.request as urllib2
import json

while True:
    ip=input("What is your target IP: ")
    url="http://ip-api.com/json/"

    response=urllib2.urlopen(url+ip)
    data=response.read()
    values=json.loads(data)
    
    print("IP: "+values["query"])
    print("ISP: "+values["isp"])
    print("City: "+values["city"])
    print("Region: "+values["region"])
    print("Country: "+values["country"])
    print("Timezone: "+values["timezone"])
    break