#!/usr/bin/env python2

import requests

urls = ['http://cpt.hopper.pw:LBbRhmu3gV@ipv4.www.hopper.pw/nic/update', 'http://%3Cyour%20fqdn%3E:%3Cyour%20secret%3E@ipv6.www.hopper.pw/nic/update']

# basic auth to hopper.pw updates
for url in urls:
	try:
		r = requests.get(url, auth=('cpt.hopper.pw', 'LBbRhmu3gV'))
		print r.text
	except requests.exceptions.RequestException as e:
		print "Error %s" % e
