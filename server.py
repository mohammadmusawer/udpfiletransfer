import socket                                                               #module to establish connection
socketVar = socket.socket()                                                 #initialization of the socket object

hostName = socket.gethostname()                                             #initialization of server address
port = 8090                                                                 #set server port to 8090
socketVar.bind((hostName, port))                                            #bind server to host/port
socketVar.listen(1)                                                         #wait for 1 incoming connection

print(hostName)                                                             #display host name
print("Waiting for connection...")                                          #display server is waiting for connection

connection, address = socketVar.accept()                                    #accept incoming connection

print(address, "Has connected to the server")                               #display the connected server address

fileName = input(str("Input name of the file to be transferred: "))         #ask for name of file to be transferred
file = open(fileName, 'rb')                                                 #open file in read-binary
data = file.read(500000)                                                    #read file
connection.send(data)                                                       #send the read file

print("Data has been transmitted successfully")                             #display that data has been transferred
