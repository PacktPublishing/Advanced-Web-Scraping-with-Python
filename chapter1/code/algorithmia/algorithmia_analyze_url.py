#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Algorithmia
import json

input = [ "https://www.packtpub.com/iot-hardware/single-board-computers"]
output = []

API_KEY ='simU+xQFB6Ts4O306dxEhZreKBA1'

client = Algorithmia.client(API_KEY)

algorithmia = client.algo('web/AnalyzeURL/0.2.17').pipe(input[0])
print(algorithmia.result)
output.append(algorithmia.result)
print(json.dumps(output, indent=4))