import socket
localIP     = "127.0.0.1"

localPort   = 20001

bufferSize  = 1024

msgFromServer       = "    Hello UDP Client"

bytesToSend         = str.encode(msgFromServer)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
message = bytesAddressPair[0]
address = bytesAddressPair[1]
clientMsg = "Message from Client:     {}".format(message)
clientIP  = "Client IP Address:       {}".format(address)
print(clientMsg)
print(clientIP)
UDPServerSocket.sendto(bytesToSend, address)

while(True):
    data, addr = UDPServerSocket.recvfrom(1024)
    print ("Message:   " + data.decode())

bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
message = bytesAddressPair[0]
address = bytesAddressPair[1]
clientMsg = "Message from Client:      {}".format(message)
clientIP  = "Client IP Address:        {}".format(address)
print(clientMsg)
print(clientIP)
UDPServerSocket.sendto(bytesToSend, address)