import socket

SRV_ADDR = input("Please type in the serve IP Address: ")
SRV_PORT = int(input("Please type in the server port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SRV_ADDR, SRV_PORT))
print("Connection established.")

message = input("Send everybody a message: ")
s.sendall(message.encode())
s.close()