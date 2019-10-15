#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanicalsoup
import getpass

URL = "https://twitter.com/login"
    
username = input ("Username: ")
password = getpass.getpass()

# Create a browser object
browser = mechanicalsoup.Browser()

# request Twitter login page
login_page = browser.get(URL)

# we grab the login form
login_form = login_page.soup.find("form", {"class":"t1-form clearfix signin js-signin"})

# find login and password inputs
login_form.find("input", {"name": "session[username_or_email]"})["value"] = username
login_form.find("input", {"name": "session[password]"})["value"] = password

# submit form
browser.submit(login_form, login_page.url)