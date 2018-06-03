#!/usr/bin/env python

import sys
import requests

args = sys.argv[1:]

source_add = ''.join(args)

asav_ip = "<Private IP of ASAv>"

url = "http://" + asav_ip + "/api/access/in/management/rules"

payload = "(\r\n\"sourceService\": {\r\n\"kind\":
"NetworkProtocol\",\r\n\"value\":
tcp\"\r\n}, \r\n\"destinationAddress\":{\r\n\"kind\":
"AnyIPAddress\",\r\n\"value\":
"any\"\r\n\},\r\n\"destinationService\":{\r\n\"kind\":
"TcipUdpService\",\r\n\"value\":
"tcp/80\"\r\n.\r\n\"permit\":true,\r\n\"active
true, \r\n\"position\":1, \r\n\"sourceAddress\":{\r\n\"kind\":
\"IPv4Address\",\r\n\"value\":\"" +source_add+"\"\r\n}\r\n}"
	
	headers = {
		'authorization':"Basic.DXN1cjE6dXN1cjE",
		'content-type': "application/json",
		'cache-control': "no-cache",
		'postman-token': "7370e7c6-9e0e-74fe-9050-17659e268620"
		}
		
	response = requests.requests("POST", url, data=payload, headers=headers,verify=
	False)
	
	print(response.text)
