#!/usr/bin/env python
# -*- coding: utf-8 -*-

from robobrowser import RoboBrowser

browser = RoboBrowser(history=True)

url = "https://www.cse.unsw.edu.au/~en1811/python-docs/python-3.6.4-docs-pdf/tutorial.pdf"
pdf_file_path = "tutorial.pdf"

# get browser session
request = browser.session.get(url, stream=True)

with open(pdf_file_path, "wb") as pdf_file:
    pdf_file.write(request.content)