#!/usr/bin/python3

import socket, sys, signal, time

if len(sys.argv) != 2:
	print(f"\nUsage: python3 {sys.argv[0]} <port>")
	sys.exit()

port = sys.argv[1]

def server():
	global server, keys, result
	count = 0
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
		server.bind(("", int(port)))
		server.listen()
		print(f"Server Started at {time.strftime('%A %d/%m/%Y %X')} on port {port}")
		conn, addr = server.accept()
		print(f"Connected with {addr[0]} on port {addr[1]}\n")
		while True:
			try:
				result = conn.recv(49049).decode()
				if "Ending key: GwE" in result:
					count += 1
					if count > 1:
						print(f"\nConnection finished at {time.strftime('%A %d/%m/%Y %X')}")
						server.close()
						f.close()
						time.sleep(1)
						sys.exit()
				if result:
					f.write(result)
					print(result, end="", flush=True)
				result = ""
			except ConnectionResetError:
				print(f"\nConnection finished at {time.strftime('%A %d/%m/%Y %X')}")
				server.close()
				f.close()
				sys.exit()


def def_handler(signum, frame):
	print("\n[*] Exiting...\n\n")
	f.close()
	server.close()
	sys.exit()

signal.signal(signal.SIGINT, def_handler)

if __name__ == '__main__':
	f = open(f"serverData {time.strftime('%A %d-%m-%Y %X')}".replace(":", "_"), "w", encoding="utf-8")
	f.write(f"Started at {time.strftime('%d/%m/%Y %X')}\n")
	server()
