import socket   #My Name: Farhaan Jiwa, My Partner: Carrau Brewer 

testsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create testsocket1
testsocket.bind(('192.168.1.65', 3310))  #Bind testsocket1 to ip and port

testsocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create testsocket 2
testsocket2.bind(('192.168.1.65', 12345)) #Bind testsocket2 to ip and port

testsocket.listen(5)

print('Robot is started') #this lets us know the robot is ready to initiate contact with client

(client,(ip,port)) = testsocket.accept() #testsocket1 accepts client and gathers ip and port information
print('Got connection from', ip) #print connection from client IP

while (True):
        Data = client.recv(2048).decode() #Here the program decodes any message sent by the client
        print ("C:",Data)                                               #print data received from client
        sendData =("S: 12345")                                          #server prepares to send message to client
        client.send(sendData.encode())                                  #encode and send data to client

        break

testsocket2.listen(4)

testsocket.close()
    
print('TCP socket 2 is started')
(client,(ip,port)) = testsocket2.accept()
print('Got connection from', ip)

UDP1AND2 = ("S: ffffff, eeeeee")    #send message to client for new UDP connections

client.send(UDP1AND2.encode())


testsocket2.close() #close testserver2 and the start of the udp portion

ip = "192.168.1.65";
port = 1648;
listeningAddress = (ip, port);
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind(listeningAddress);
print("UDP socket 1 up and listening")

while (True):

    numberstring, addr = UDPServerSocket.recvfrom(256)
    print("Number recived", (numberstring.decode()));
    
    break

print("UDP socket 1 on hold")   #print UDP port on hold as we will come back to it later in the assignment

host2 = "192.168.1.65"
port2 = 5000
serveraddress = (host2, port2)
UDPServerSocket2 = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)

print("UDP socket 2 up and listening")

UDPServerSocket2.bind(("192.168.1.65", 2000))

data = b"The number is 70"

UDPServerSocket2.sendto(data, ("192.168.1.66", 1649))    #supposed to be sent 5 times but only recieved once on the client end once
UDPServerSocket2.sendto(data, ("192.168.1.66", 1649))
UDPServerSocket2.sendto(data, ("192.168.1.66", 1649))
UDPServerSocket2.sendto(data, ("192.168.1.66", 1649))
UDPServerSocket2.sendto(data, ("192.168.1.66", 1649))
UDPServerSocket2.sendto(data, ("192.168.1.66", 1649))

print("UDP socket 2 Closed")

UDPServerSocket2.close()


#-------------------------------------------

print("UDP socket 1 up and listening")

while (True):

    FromClient, addr = UDPServerSocket.recvfrom(256)
    print("Number recived", (FromClient.decode())); #only supposed to be recieved once but client will send it 5 times
    if FromClient == FromClient:
        break

print("UDP socket 1 closing")


UDPServerSocket.close()

