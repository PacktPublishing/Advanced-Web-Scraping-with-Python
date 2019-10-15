#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import os, sys
import requests
from fake_useragent import UserAgent

def getAllImages(url):

    ua = UserAgent()
    header = {'user-agent':ua.chrome}
    schedule_page = requests.get(url,headers=header)

    #create directory for save images
    os.system("mkdir images_packtpub")

    bs = BeautifulSoup(schedule_page.text,"lxml")
    for image in bs.findAll("img"):
        print("found image")

        #Extract the location of the image. We also need to strip for get the image name, so let's do that through '.split()'
        src = image.get('src')
        print(src)

        parts_image = src.split("/")
        image_name = parts_image[len(parts_image)-1]

        #Save the image
        with open("images_packtpub/"+image_name,"wb") as f:
            f.write(requests.get(src).content)

getAllImages("http://www.packtpub.com")
