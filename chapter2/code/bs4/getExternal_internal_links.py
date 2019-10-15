#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import re
import requests
import argparse

internalLinks = []
externalLinks = []

#Get a list of internal links that start with a "/"
def getInternalLinks(url,beautifulSoup):
    url = url.replace("http://", "").split("/")[0]
    for link in beautifulSoup.findAll("a", href=re.compile("^(/|.*"+url+")")):
        if link.attrs['href'] is not None:
            internalLinks.append(link.attrs['href'])
    return internalLinks


#Get all links that start with "http" or "www" and not contain the current URL
def getExternalLinks(url,beautifulSoup):
    url = url.replace("http://", "").split("/")[0]
    for link in beautifulSoup.findAll("a", href=re.compile("^(http|www)((?!"+url+").)*$")):
        if link.attrs['href'] is not None:
            externalLinks.append(link.attrs['href'])
    return externalLinks


def crawlExternalLinks(website):
    html = requests.get(website)
    beautifulSoup = BeautifulSoup(html.text,"lxml")
    externalLinks = getExternalLinks(website, beautifulSoup)
    return externalLinks

def crawlInternalLinks(website):
    html = requests.get(website)
    beautifulSoup = BeautifulSoup(html.text,"lxml")
    internalLinks = getInternalLinks(website,beautifulSoup)
    return internalLinks

def getExternalInternalLinks(website):
    externalLinks = crawlExternalLinks(website)
    internalLinks = crawlInternalLinks(website)
    print("\nExternal links")
    print("-------------------")

    for external in externalLinks:
        print(external)

    print("\nInternal links")
    print("-------------------")    
    for internal in internalLinks:
        print(internal)


if __name__== "__main__":

    # parse the command line arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-d","--domain",required=True,help="The domain to target ie. packtpub.com")
    args = vars(ap.parse_args())

    domain = args['domain']

    if domain.startswith("http://") == True:
        target = domain
    else:
        target = "http://" + domain

getExternalInternalLinks(target)