# Import necessary Libraries

import threading as th
import socket
import sys
import struct

def dns_query(hostname):
	server = '8.8.8.8'  # Google server
	serverPort = 53
	print('Hostname:', hostname)
	# Recursive Query sent to DNS
	query = bytes("\x12\x12" +
				   "\x01\x00" +
				   "\x00\x01" +
				   "\x00\x00" +
				   "\x00\x00" +
				   "\x00\x00", 'utf-8')
	d = bytes("", 'utf-8')

	# Construct hostname into Query
	for a in hostname.split('.'):
		d += struct.pack("!b" + str(len(a)) + "s", len(a), bytes(a, "utf-8"))
	query = query +  d +  bytes("\x00", 'utf-8')  # terminate domain with zero len
	query = query + bytes("\x00\x01" + "\x00\x01", 'utf-8')  # type A, class IN
	print('DNS query is:', query)

	# Open UDP socket to send DNS query to Google
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(query, (server, serverPort))

	# Get reply from Google on UDP socket
	reply, addr = sock.recvfrom(2048)
	print('DNS response:', str(reply), len(reply))
	# Extract IP from reply message
	print('Converted response:', list(reply))
	ip = ""
	for i in range(1,5):
		ip = "."+str(reply[-1*i])+ip
	ip = ip[1:]
	http_query(ip, hostname)

def http_query(ip, hostname):
	# Open TCP socket to send HTTP query
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, 80))
	print('Connection has been established!')

	# Construct HTTP query send over socket
	message = "GET / HTTP/1.1\r\n"
	message += f"HOST: {hostname}\r\n"
	message += "User-Agent: Firefox/86\r\n"
	message += "\r\n"
	x = s.send(message.encode())
	print('Message size:'+ str(x) + ' bytes')

	# Get reply from HTTP on TCP socket
	data = s.recv(4096).decode()
	save_files(data, hostname)

def save_files(data, hostname):
	f = open(f"{hostname}.html", "w", encoding="utf-8")
	for i in data:
		f.write(i)

# Collect all hostnames in a list in order to run all
hostnames = []
for i in range(1, len(sys.argv)):
	hostnames.append(sys.argv[i])
a = 1
for hostname in hostnames:
	dns_query(hostname)
	a+=1