#!/usr/bin/env python3

import requests, datetime
from time import sleep

urls = ['http://cpt.hopper.pw:LBbRhmu3gV@ipv4.www.hopper.pw/nic/update']

# basic auth to hopper.pw updates
while True:
	for url in urls:
		try:
			r = requests.get(url, auth=('cpt.hopper.pw', 'LBbRhmu3gV'))
			print("response @", datetime.datetime.now(), ":", r.text)
		except requests.exceptions.RequestException as e:
			print(e, file=sys.stderr) # print to stderr
	sleep(300) # sleep for five minutes
