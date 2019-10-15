#!/usr/bin/env python
# -*- coding: utf-8 -*-

from robobrowser import RoboBrowser
import re
import argparse

browser = RoboBrowser(history=True,parser="html.parser")

def get_emails(domain):
	
	domain="http://"+domain
	browser.open(domain)
	contents = browser.find_all("a",href=re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+"))
	for content in contents:
		print(content['href'])
		
def get_links(domain):
	
	domain="http://"+domain
	browser.open(domain)
	
	print('*****browser.find_all("a")******\n')
	contents = browser.find_all("a")
	for content in contents:
		try:
			print(content['href'])
		except Exception as exception:
			pass

	print('*****browser.get_links()******\n')
	links = browser.get_links()
	for link in links:
		try:
			print(link['href'])
		except Exception as exception:
			pass
    
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='gets emails from domain.', prog='get_emails_links_from_url.py', epilog="", add_help=False)
	parser.add_argument('-d', '--domain', metavar='<domain>', action='store', help='domain to be resolved.',required=True)
	args = parser.parse_args()
	get_emails(args.domain)
	get_links(args.domain)