#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanicalsoup

# Connect to bing search engine
browser = mechanicalsoup.StatefulBrowser()
browser.open("http://bing.com/")

# Fill-in the search form
browser.select_form('#sb_form')
browser["q"] = "MechanicalSoup"
browser.submit_selected()

# Display the results
for link in browser.links():
    print(link.text, '->', link.attrs['href'])
