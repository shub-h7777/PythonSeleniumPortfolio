import requests
import config

""" for get/read the responses"""

# get the endpoint
url = config.users()

r = requests.get(url)
print(r.status_code)    #for status code
print(r.text)           #for text/string
print(r.json())         #for JSON
