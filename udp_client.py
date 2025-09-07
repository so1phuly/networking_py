import socket

tagret_host = "0.0.0.0"
tagret_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("AAABBBCCC".encode(), (tagret_host, tagret_port))

data, addr = client.recvfrom(4096)

print(data.decode())