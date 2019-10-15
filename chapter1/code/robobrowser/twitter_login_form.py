#!/usr/bin/env python
# -*- coding: utf-8 -*-

from robobrowser import RoboBrowser

browser = RoboBrowser(history=True,parser="html.parser")
browser.open('http://twitter.com/login')
print(browser.parsed)

# Get the signup form by action or css class
signup_form = browser.get_form(action="https://twitter.com/sessions")
signup_form = browser.get_form(class_='t1-form clearfix signin js-signin')
print(signup_form)

# Inspect authenticity_token value
print(signup_form['authenticity_token'].value)

# Fill it out
signup_form['session[username_or_email]'].value = 'username'
signup_form['session[password]'].value = 'password'

print(signup_form.serialize())

# Submit the form
browser.submit_form(signup_form)