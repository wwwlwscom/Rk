#!/usr/bin/env python

import sys, smtplib, socket
from getpass import getpass

fromaddr = 'wwwlwscom@163.com'
toaddr = sys.argv[1]

message = """To: %s
From: %s
Subject: Test message from simple.py

Hello,

This is a test message sent to you from simple.py and smtplib.
""" % (', '.join(toaddr), fromaddr)

password = getpass("Enter Password:")


try:
	s = smtplib.SMTP('smtp.163.com')
	code = s.ehlo()[0]
	usesesmtp = 1
	if not (200 <= code <= 299):
		usesesmtp = 0
		code = s.helo()[0]
		if not (200 <= code <= 299):
			raise SMTPHeloError(code, resp)
	if usesesmtp and s.has_extn('starttls'):
		print "Negotiating TLS...."
		s.starttls()
		code = s.ehlo()[0]
		if not (200 <= code <= 299):
			print "Couldn't EHLO after STARTTLS"
			sys.exit(5)
		print "Using TLS connection."
	else:
		print "Server does not support TLS; using normal connection."
	s.login(fromaddr,password)
	s.set_debuglevel(1)
	s.sendmail(fromaddr, toaddr, message)
except (socket.gaierror,socket.error,socket.herror,smtplib.SMTPException), e:
	print " *** Your message may not have been sent!"
	print e
	sys.exit(1)
else:
	print "Message successfully sent to  %d recipient(s)" % len(toaddr)

