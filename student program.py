import socket    #My Name: Farhaan Jiwa, My Partner: Carrau Brewer 
from random import randint

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('192.168.1.65', 3310))

str = input("C: ")
clientsocket.send(str.encode()); 
print (clientsocket.recv(1024).decode())

clientsocket.close()
#------------------------------

clientsocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket2.connect(('192.168.1.65', 12345))

print (clientsocket2.recv(1024).decode())

clientsocket2.close()
#-----------------------
#create a UDP socket
ip = "192.168.1.65"
port = 1648
ServerAddress = ("192.168.1.65", 1648)
msgFromClient = "7"

buffersize = 1024

UDPclientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


UDPclientsocket.sendto(msgFromClient.encode('utf-8'), ServerAddress)

#-------------------------
host = '192.168.1.65';
port = 7000;
ServerAddress2 = (host, port)
UDPclientsocket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPclientsocket2.bind(("192.168.1.66", 1649))

while(True):
    data = UDPclientsocket2.recv(512)
    print(data.decode('utf-8'))
    if data == data:
        break
UDPclientsocket2.close()

#supposed to recieve 5 times but only print once and close socket
#------------------------------------------
FromClient = "is 70"

UDPclientsocket.sendto(FromClient.encode('utf-8'), ServerAddress)
UDPclientsocket.sendto(FromClient.encode('utf-8'), ServerAddress)
UDPclientsocket.sendto(FromClient.encode('utf-8'), ServerAddress)
UDPclientsocket.sendto(FromClient.encode('utf-8'), ServerAddress)
UDPclientsocket.sendto(FromClient.encode('utf-8'), ServerAddress)

UDPclientsocket.close()

#supposed to be send 5 times









