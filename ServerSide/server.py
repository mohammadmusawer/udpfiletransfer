import socket                        #module to establish connection
socketVar = socket.socket()          #initialization of the socket object

hostName = socket.gethostname()      #initialization of server address
port = 8090                          #set server port to 8090
socketVar.bind((hostName, port))     #bind server to host/port
socketVar.listen(1)                  #wait for 1 incoming connection

print(hostName)                      #display host name

while True:
    print("Waiting for connection...")
    connection, address = socketVar.accept()  # accept incoming connection

    print(address, "Has connected to the server")  # display the connected server address

    fileName = connection.recv(1024)  # receive data from connection setting buffer to 1024 bytes
    print(fileName)  # display the file name
    fileName = fileName.decode()  # decode the file name
    numOfPackets = connection.recv(1024)  # set the number of packets to receive data from connection
    decodedNumOfPackets = numOfPackets.decode()  # decode number of packets
    numOfPackets = int(decodedNumOfPackets)  # return number of packets as an integer

    file = open(fileName, 'wb')  # open the file in write-binary

    # loops to keep receiving packets and prints the packets being received from the client
    for x in range(1, numOfPackets + 1):
        numOfPacketsRecv_String = f"Receiving packet #{x} from client..."
        print (numOfPacketsRecv_String)
        data = connection.recv(1024)
        file.write(data)
    connection.close()
    file.close()

    print("\nData has been transmitted successfully!")  # display that data has been transferred
    break  # end the program after transmitting file