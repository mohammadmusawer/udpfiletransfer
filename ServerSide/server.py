import socket                                                               #module to establish connection
socketVar = socket.socket()                                                 #initialization of the socket object

hostName = socket.gethostname()                                             #initialization of server address
port = 8090                                                                 #set server port to 8090
socketVar.bind((hostName, port))                                            #bind server to host/port
socketVar.listen(1)                                                         #wait for 1 incoming connection

print(hostName)                                                             #display host name

while True:
    print("Waiting for connection...")
    connection, address = socketVar.accept()  # accept incoming connection

    print(address, "Has connected to the server")  # display the connected server address

    fileName = connection.recv(1024)
    print(fileName)
    fileName = fileName.decode()
    numOfPackets = connection.recv(1024)
    decodedNumOfPackets = numOfPackets.decode()
    numOfPackets = int(decodedNumOfPackets)

    file = open(fileName, 'wb')

    for x in range(0, numOfPackets):
        data = connection.recv(1024)
        file.write(data)
    connection.close()
    file.close()

    print("Data has been transmitted successfully")  # display that data has been transferred

