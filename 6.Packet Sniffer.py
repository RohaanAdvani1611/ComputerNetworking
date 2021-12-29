import socket
import struct
import textwrap
import sys


def main():
	# Take command line arguments from user
	length = len(sys.argv)
	i=1
	if length == 3:
		dest_add = sys.argv[i]
		dest_pt = sys.argv[i+1]

	elif length == 4:
		dest_add = sys.argv[i]
		dest_pt = sys.argv[i+1]
		prot = sys.argv[i+2]
		if prot =='ICMP':
			val = 1
		elif prot == 'TCP':
			val = 6
		elif prot == 'UDP':
			val = 17;
		else: 
			val = 0;
		
	else: 
		print('Incorrect number of arguments')
		sys.exit(0)
	
	# Start Socket	
	s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
	if length == 4:
		while True:
			raw_data, addr = s.recvfrom(65536)
			dest, src, eth_prot, data = unpack_eth(raw_data)
			if eth_prot == 8:
				(version, header_len, ttl, prot, src, dest, data) = unpack_ipv4(data)
				#if dest == dest_add and (val == prot or val == 0):
				if True:
					if prot == 1:
						icmp_type, code, checksum, data = unpack_icmp(data)
						print('\nEth Frame: Dest: {}, Src: {}, Prot: {}'.format(dest, src, eth_prot))
						print('ICMP Packet: Type: {}, Code: {}, Checksum: {}'.format(icmp_type, code, checksum))
						print(data)
					elif prot == 6:
						(s_pt, d_pt, sequence, acknowledgement, fl_urg, fl_ack, fl_psh, fl_rst, fl_syn, fl_fin, data) = unpack_tcp(data)
						#if d_pt == dest_pt:
						if True:
							print('\nEth Frame: Dest: {}, Src: {}, Prot: {}'.format(dest, src, eth_prot))
							print('TCP Segment: Src Port: {}, Dest Port: {}'.format(s_pt, d_pt))
							print('Seq: {}, Ack: {}'.format(sequence, acknowledgement))
							print('Flags: U: {}, A: {}, P: {}, R: {}, S: {}, F: {}'.format(fl_urg, fl_ack, fl_psh, fl_rst, fl_syn, fl_fin))
							print(data)
						else:
							continue
					elif prot == 17:
						s_pt, d_pt, length, data = unpack_udp(data)
						#if d_pt == dest_pt:
						if True:
							print('\nEth Frame: Dest: {}, Src: {}, Prot: {}'.format(dest, src, eth_prot))
							print('UDP Segment: Src Port: {}, Dest Port: {}, Len: {}'.format(s_pt, d_pt, length))
						else:
							continue
							
					else:
						print('\nEth Frame: Dest: {}, Src: {}, Prot: {}'.format(dest, src, eth_prot))
						print(data)
				else:
					continue
	else:
		while True:
			raw_data, addr = s.recvfrom(65536)
			dest, src, eth_prot, data = unpack_eth(raw_data)
			if eth_prot == 8:
				
				(version, header_len, ttl, prot, src, dest, data) = unpack_ipv4(data)
				#if dest == dest_add:
				if True:					
					if prot == 1:
						icmp_type, code, checksum, data = unpack_icmp(data)
						print('\nEth Frame: Dest: {}, Src: {}, Prot: {}'.format(dest, src, eth_prot))
						print('ICMP Packet: Type: {}, Code: {}, Checksum: {}'.format(icmp_type, code, checksum))
						print(data)
					elif prot == 6:
						(s_pt, d_pt, sequence, acknowledgement, fl_urg, fl_ack, fl_psh, fl_rst, fl_syn, fl_fin, data) = unpack_tcp(data)
						#if d_pt == dest_pt:
						if True:
							print('\nEth Frame: Dest: {}, Src: {}, Prot: {}'.format(dest, src, eth_prot))
							print('TCP Segment: Src Port: {}, Dest Port: {}'.format(s_pt, d_pt))
							print('Seq: {}, Ack: {}'.format(sequence, acknowledgement))
							print('Flags: U: {}, A: {}, P: {}, R: {}, S: {}, F: {}'.format(fl_urg, fl_ack, fl_psh, fl_rst, fl_syn, fl_fin))
							print(data)
						
					elif prot == 17:
						s_pt, d_pt, length, data = unpack_udp(data)
						#if d_pt == dest_pt:
						if True:
							print('\nEth Frame: Dest: {}, Src: {}, Prot: {}'.format(dest, src, eth_prot))
							print('UDP Segment: Src Port: {}, Dest Port: {}, Len: {}'.format(s_pt, d_pt, length))
												
					else:
						print('\nEth Frame: Dest: {}, Src: {}, Prot: {}'.format(dest, src, eth_prot))
						print(data)


def unpack_eth(data):
	dest, src, prot = struct.unpack('! 6s 6s H', data[:14])
	return get_address(dest), get_address(src), socket.htons(prot), data[14:]
	
def unpack_ipv4(data):
	ver_h_length = data[0]
	ver = ver_h_length >> 4
	h_length = (ver_h_length & 15) * 4
	ttl, prot, src, dest = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
	return ver, h_length, ttl, prot, ipv4_add(src), ipv4_add(dest), data[h_length:]
	
def unpack_icmp(data):
	icmp_type, code, checksum = struct.unpack('! B B H', data[:4])
	return icmp_type, code, checksum, data[4:]

def get_address(bytes_addr):
	bytes_str = map('{:2x}'.format, bytes_addr)
	return ':'.join(bytes_str).upper()

def ipv4_add(addr):
	return '.'.join(map(str, addr))

def unpack_tcp(data):
	(s_pt, d_pt, sequence, acknowledgement, flags) = struct.unpack('! H H L L H', data[:14])
	offset = (flags >> 12) * 4
	fl_urg = (flags & 32) >> 5
	fl_ack = (flags & 16) >> 4
	fl_psh = (flags & 8) >> 3
	fl_rst = (flags & 4) >> 2
	fl_syn = (flags & 2) >> 1
	fl_fin = flags & 1
	return s_pt, d_pt, sequence, acknowledgement, fl_urg, fl_ack, fl_psh, fl_rst, fl_syn, fl_fin, data[offset:]

def unpack_udp(data):
	s_pt, d_pt, size = struct.unpack('! H H 2x H', data[:8])
	return s_pt, d_pt, size, data[8:]


main()
