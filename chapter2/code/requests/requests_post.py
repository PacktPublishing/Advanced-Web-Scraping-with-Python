#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
data_dictionary = {'name': 'username','password': '123456','email': 'user@domain.com'}
response = requests.post("http://httpbin.org/post",data=data_dictionary)

if response.status_code == 200:
	print(response.text)