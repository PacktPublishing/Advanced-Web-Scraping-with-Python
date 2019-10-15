#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from fake_useragent import UserAgent

url = 'https://www.packtpub.com'
file_name = 'packtpub.com.txt'

user_agent = UserAgent()
page = requests.get(url,headers={'user-agent':user_agent.chrome})
print(page.content)
with open(file_name,'w') as file:
    file.write(page.content.decode('utf-8')) 