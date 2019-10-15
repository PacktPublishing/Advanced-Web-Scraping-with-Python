#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json
from fake_useragent import UserAgent

ua = UserAgent()
header = {'user-agent':ua.chrome}

responseGet = requests.get("https://www.packtpub.com",headers=header)
print(responseGet.text.encode('utf-8'))
print(responseGet.json)
print(responseGet.encoding)
print(responseGet.content)
print("Status code: "+str(responseGet.status_code))

print("Headers response: ")
for header, value in responseGet.headers.items():
  print(header, '-->', value)
 
print("Headers request : ")
for header, value in responseGet.request.headers.items():
  print(header, '-->', value)