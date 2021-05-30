import socket

msgFromClient       = "   Hello UDP Server".encode()

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("127.0.0.1", 20001)

bufferSize          = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Message from Server {}     ".format(msgFromServer[0])
print(msg)

while True:
    msg = str(input("Enter your message::  "))
    msg = msg.encode()
    UDPClientSocket.sendto(msg, (serverAddressPort))

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Message from Server {}     ".format(msgFromServer[0])

print(msg)

