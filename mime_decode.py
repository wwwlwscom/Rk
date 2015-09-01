#!/usr/bin/env python

import sys, email

counter = 0
parts = []

def printmsg(msg, level = 0):
	global counter
	l = "| " * level
	ls = l + "*"
	l2 = l + "|"
	if msg.is_multipart():
		print l + "Found multipart:"
		for item in msg.get_payload():
			printmsg(item, level + 1)
	else:
		disp = ['%d. Decodable part' % (counter + 1)]
		if 'content-type' in msg:
			disp.append(msg['content-type'])
		if 'content-diaposition' in msg:
			disp.append(msg['content-disposition'])
		print l + ", ".join(disp)
		counter += 1
		parts.append(msg)

imputfd = open(sys.argv[1])
msg = email.message_from_file(inputfd)
printmsg(msg)

while 1:
	print "Select part number to decode or q to quit:"
	part = sys.stdin.readline().strip()
	if part == 'q':
		sys.exit(0)
	try:
		part = int(part)
		msg = parts[part - 1]
	except:
		print "Invalid selections."
		continue

	print "Select file to write to:"
	filename = sys.stdin.readline().strip()
	try:
		fd = open(filename, 'wb')
	except:
		print "Invalid filename."
		continue

	fd.write(msg.get_payload(decode = 1))



