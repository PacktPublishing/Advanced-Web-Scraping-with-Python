#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Algorithmia

input = [ "http://packtpub.com",1]

API_KEY ='simU+xQFB6Ts4O306dxEhZreKBA1'

client = Algorithmia.client(API_KEY)
response = client.algo('web/SiteMap/0.1.7').pipe(input)
siteMap = response.result
print(siteMap)