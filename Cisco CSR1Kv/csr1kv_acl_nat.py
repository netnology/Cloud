#!/usr/bin/env python

import sys
import json
import requests

args = sys.argv[1:]

source_add = ''.join(args)

csr1kv_ip = "<Private IP of CSR1Kv>"

acl = "NATList"

def auth_token():
	
	url = "http://" + csr1kv_ip + ":55443/api/v1/auth/token-services"
	
	headers = {
		'authorization':"Basic.DXN1cjE6dXN1cjE",
		'cache-control': "no-cache",
		'postman-token': "7370e7c6-9e0e-74fe-9050-17659e268620"
		}
		
	response = requests.requests("POST", url, headers=headers,verify=
	False)
	token = j.son.loads(response.text)
	token1 = token["token-id"]
	return token1

