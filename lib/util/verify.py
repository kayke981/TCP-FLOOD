import nmap, socket, time
from lib.util.debug import Debug, colors

def check(ip):
	scanner = nmap.PortScanner()
	host = socket.gethostbyname(ip)
	scanner.scan(host)
	status = scanner[host].state().replace('up', f'{colors.reset}{colors.green}ONLINE{colors.reset}').replace('down', f'{colors.reset}{colors.red}OFFLINE{colors.reset}')
	Debug(f'[*] Host status {status}')