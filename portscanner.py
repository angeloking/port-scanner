#!/usr/bin/python

print '##########################################################'
print '#                                                        #'
print '#                                                        #'
print '#                                                        #'
print '#		PORT SCANNER                            #'
print '#			--Coded By Angelo King          #'
print '#                                                        #'
print '#                                                        #'
print '#                                                        #'
print '##########################################################'


import socket
import sys
import time
import subprocess
import datetime
import threading

url = raw_input('Enter the host you wants to scan: ')
url = url.replace('http://','')	
	
def getip(host):
	tx = socket.gethostbyname(host)
	return tx

def scan(port):
	tl = getip(url)
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		response = sock.connect_ex((tl, port))
		if response == 0:
			print 'Port open: %d'%port
		sock.close()
	except socket.error:
		print 'Unable to connect to server'
		sys.exit()
	except socket.gaierror:
		print 'Hostname could not be resolved. Exiting'
		sys.exit()
	
def getport():
	threads = []
	for i in range(1, 4000):
		t = threading.Thread(target=scan, args=(i,))
		threads.append(t)
		t.start()

def main():
	subprocess.call('clear', shell='True')
	tm = getip(url)
	print '-'*60
	print 'Please wait, scanning remote host: ' + tm
	print '-'*60
	time.sleep(3)
	t1 = datetime.datetime.now()
	print t1
	try:
		getport()
	except KeyboardInterrupt:
		print 'Exiting...'
		sys.exit()
main()
