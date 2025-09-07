import socket

tagret_host = "www.google.com"
tagret_port = 80

# tạo một socket obj
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# kết nối client đến server
client.connect((tagret_host, tagret_port))

# gửi một số dữ liệu
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# nhận dữ liệu từ server
response = client.recv(4096)

print(response.decode())