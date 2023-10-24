'''
Set of functions that interface with Grandstream GDMS Cloud

'''

import requests
import json
import logging

# Logging config
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s',)

def makeRequest():
    request = requests.get('https://www.gdms.cloud/oapi/oauth/token', params={'username': 'username', 'password': 'password', 'grant_type': 'password'})
    print(request)
    print(request.text)