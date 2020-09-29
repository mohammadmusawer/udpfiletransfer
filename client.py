import socket                                                          #module to establish connection

socketVar = socket.socket()                                            #initialization of the socket object
hostAddress = input(str("Input host address: "))                       #ask user to input host address to connect
port = 8090                                                            #set client port to 8090
socketVar.connect((hostAddress, port))                                 #connect to host address

print("Connected...")                                                  #display connected to host address

fileName = input(str("Input name for the incoming file: "))            #ask user for a name for the incoming file
file = open(fileName, 'wb')                                            #open file in write-binary
data = socketVar.recv(500000)                                          #read the data from the file
file.write(data)                                                       #write the data into a new file
file.close()                                                           #close file

print("File has been received.")                                       #display that the file has been received
