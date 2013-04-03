#!/usr/bin/python

import unittest
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

import sys
#print(sys.path)
#sys.path.append("/usr/lib/python2.7/dist-packages/")
#sys.path.append("/usr/lib/python2.7/dist-packages/scapy/")
#print(sys.path)
from scapy.all import *

host = "127.0.0.1"
number = int(input("Enter number of pings: "))

class TestPing:
	def pingICMP(self,host, number):
		i = 0
		p = (IP(dst=host)/ICMP())
		p.show()
		while i < number:
			response = sr1(p)
#			response.show()
			i += 1
#	pingICMP(host, number)
'''
	def pingUDP(host, number):
	   	i = 0
		p = (IP(dst=host)/UDP())
			   	p.show()
		while i < number:
				response = sr1(p)
#					  	response.show()
 				i += 1
#	pingUDP(host, number)

		def pingHTTP(host, number):
				i = 0
				p = (IP(dst=host)/'GET / HTTP/1.1\r\n\r\n')
				p.show()
				while i < number:
					response = sr1(p)
#					   response.show()
					i += 1
#		pingHTTP(host, number)
'''
pinger = TestPing()
pinger.pingICMP(host,number)
