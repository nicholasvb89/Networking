import socket

target_host = "127.0.0.1"
target_port = 90

#create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data
client.sendto("AAABBBCCC".encode(), (target_host, target_port))

#recieve some data
data, addr = client.recvfrom(4096)

print(data)
