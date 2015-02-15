#!/usr/bin/env python2

import requests, datetime

urls = ['http://cpt.hopper.pw:LBbRhmu3gV@ipv4.www.hopper.pw/nic/update', 'http://%3Cyour%20fqdn%3E:%3Cyour%20secret%3E@ipv6.www.hopper.pw/nic/update']

# basic auth to hopper.pw updates
print "==========" # log separator
print "date: %s" % datetime.datetime.now()
for url in urls:
	try:
		r = requests.get(url, auth=('cpt.hopper.pw', 'LBbRhmu3gV'))
		print r.text
	except requests.exceptions.RequestException as e:
		print "error: %s" % e
