import socket
import os
import struct

# Lấy IP hiện tại hoặc đặt IP máy bạn
host = "192.168.0.107"  # thay bằng IP thật
if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
sniffer.bind((host, 0))
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

while True:
    raw_data, addr = sniffer.recvfrom(65565)
    
    # Lấy 20 byte đầu của IP header
    ip_header = raw_data[0:20]
    iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
    
    version_ihl = iph[0]
    version = version_ihl >> 4
    ihl = version_ihl & 0xF
    ttl = iph[5]
    proto = iph[6]
    src_addr = socket.inet_ntoa(iph[8])
    dst_addr = socket.inet_ntoa(iph[9])
    
    print(f"IP Packet: {src_addr} -> {dst_addr} | Protocol: {proto} | TTL: {ttl}")
