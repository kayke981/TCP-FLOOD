from lib.src.attack import Attack
from lib.util.debug import Debug
import argparse

def parser_args():
	parser = argparse.ArgumentParser(description='Flood tcp')
	parser.add_argument('-c', '--count', type=int, help='Count of packets')
	parser.add_argument('-t', '--target', type=str, help="Target's IP")
	parser.add_argument('-p', '--port', type=int, help="Port of target")
	return parser

def menu():
	parser = parser_args()
	args = parser.parse_args()

	if args.count is None and args.target is None and args.port is None:
		print('usage: python3 flood_syn.py -t 192.345.34 -p 443 -c 600')
	Debug('[*] Starting...', verbose=True)
	Attack(ip=args.target, port=args.port, packets=args.count).attack()
if __name__ == "__main__":
	menu()