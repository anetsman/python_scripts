#! /usr/bin/python

import unittest
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

#import sys
from scapy.all import *

host = "127.0.0.1"
number = int(input("Enter number of pings: "))

class TestPing(unittest.TestCase):
	def pingICMP(host, number):
		i = 0
		p = (IP(dst='google.com')/ICMP())
		p.show()
		while i < number:
			response = sr1(p)
#			response.show()
			i += 1
	pingICMP(host, number)

	def pingUDP(host, number):
       	        i = 0
               	p = (IP(dst=host)/UDP())
               	p.show()
           	while i < number:
                       	response = sr1(p)
#                      	response.show()
                       	i += 1
	pingUDP(host, number)

        def pingHTTP(host, number):
                i = 0
                p = (IP(dst=host)/'GET / HTTP/1.1\r\n\r\n')
                p.show()
                while i < number:
                        response = sr1(p)
#                       response.show()
                        i += 1
        pingHTTP(host, number)

