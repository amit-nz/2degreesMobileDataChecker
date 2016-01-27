#!/usr/bin/env python

import dryscrape
import time

# make sure you have xvfb installed
dryscrape.start_xvfb()

2degreesUsername = '022123456'
2degreesPassword = 'passw0rd'

# set up a web scraping session
sess = dryscrape.Session(base_url = 'https://secure.2degreesmobile.co.nz')

# we dont need images
sess.set_attribute('auto_load_images', False)

# visit page and log in
sess.visit('/web/ip')

# fill the fields
fieldUsername = sess.at_xpath('//*[@id="userid"]')
fieldUsername.set(2degreesUsername)
fieldPassword = sess.at_xpath('//*[@id="password"]')
fieldPassword.set(2degreesPassword)

# Wait for a few seconds to allow the javascript to enable the login btn
time.sleep(2)

# Select & click the login button
LoginBtn = sess.at_xpath('//*[@id="login"]')
LoginBtn.click()

# Navigate to the page that has the actual usage data on it
sess.visit('/group/ip/home')

# Get the usage data
DataUsage = sess.at_xpath('//*[@id="accountSummary"]/table/tbody/tr[2]/td[1]/em')
print DataUsage.text()
