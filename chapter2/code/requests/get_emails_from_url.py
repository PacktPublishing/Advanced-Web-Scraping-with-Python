#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import argparse

def get_emails(domain):
    
    if not domain.startswith("http://") == True:
        domain="http://"+domain
    
    response = requests.get(domain)
    pattern = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")
    mails = re.findall(pattern,response.text)
    emails = str(mails)

    print(emails)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='gets emails from domain.', prog='get_emails_from_url.py', epilog="", add_help=False)
    # Adding the argument
    parser.add_argument('-d', '--domain', metavar='<domain>', action='store', help='domain to be resolved.',required=True)
    args = parser.parse_args()
    
    get_emails(args.domain)