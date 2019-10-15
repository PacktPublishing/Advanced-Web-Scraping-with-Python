#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import argparse
import builtwith

class BuiltWith():

    def __init__(self):

        self.key = '1fb25d4e-31b7-468c-8793-4ecebc3467be'
        self.url ='http://api.builtwith.com/free1/api.json'

    def module_run(self, domain):
        print("\nDomain "+domain +"\n")
        print(builtwith.parse("http://"+domain))
        payload = {'key': self.key, 'lookup': domain}
        response = requests.get(self.url, params=payload)
        json=response.json()
        print(json)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='BuiltWith')
    parser.add_argument('--domain', action="store", dest="domain",required=True)
    given_args = parser.parse_args()
    domain = given_args.domain
    builtWith  = BuiltWith();
    builtWith.module_run(domain);