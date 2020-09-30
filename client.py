import socket                                                          # module to establish connection
import tkinter as tk                                                   # module to create GUI
import time                                                            # module for time funcs such as .sleep()

def transmitFile(hostAddress, fileName):
    #function to transmit the file. Contains the code copy/pasted from phase1
    #takes as input the host address to send the file to and the name for the file upon arrival

    socketVar = socket.socket()  # initialization of the socket object
    port = 8090  # set client port to 8090
    socketVar.connect((hostAddress, port))  # connect to host address

    fileToSend = open(fileName, 'rb')  # open file in read-binary

    fileToSend.seek(0, 2)    # set offset to the beginning and seek relative to the end of file
    fileLength = fileToSend.tell()   # after seeking the file return the current position
    numOfPackets = int(fileLength / 1024) + 1   # calculate number of packets
    fileToSend.seek(0, 0)   # set offset to beginning of the file
    print(fileLength)       # display file length
    print(fileName)         # display file name
    print(numOfPackets)     # display number of packets

    encodedFileName = fileName.encode()     # encode the file name
    socketVar.send(encodedFileName)         # send the encoded file name through the socket
    time.sleep(1)                           # delay 1 second
    stringNumOfPackets = str(numOfPackets)  # convert number of packets into a string
    encodedStringNumOfPackets = stringNumOfPackets.encode()  # encode the number of packets string
    socketVar.send(encodedStringNumOfPackets)   # send the encoded string through the socket

    # loop to keep sending packets and prints the packet number that is being sent
    for x in range(1, numOfPackets + 1):
        numOfPacketsSend_String = f"Receiving packet #{x} from client..."
        print(numOfPacketsSend_String)
        data = fileToSend.read(1024)
        socketVar.send(data)
    fileToSend.close()

    print ("\nData has been sent successfully!") # Displays that the data has been sent successfully

    return

def sendFile(event):
    #event to send the file once the user has clicked the "Send file" button
    hostAddress = ent_destination.get()
    fileName = ent_fileName.get()
    print(fileName)
    window.quit()
    transmitFile(hostAddress, fileName)
    return

#Get the name of this machine to use as a default address
defaultServerName = socket.gethostname()
window = tk.Tk()
#introductory message
lbl_introduction = tk.Label(text = "Networking Design Project Phase 2. \n"
                             "EECE.4830 201. Professor Vokkarane. \n"
                             "By: Julie Dawley, Ricardo Candanedo, and Mohammad Musawer \n \n"
                             "Destination Computer: Defaults to this machine. \n"
                             "Change to the address in serverClient if running client and server on seperate machines")
lbl_introduction.pack()
#Get the destination name from the user, default to defaultServerName
ent_destination = tk.Entry()
ent_destination.pack()
ent_destination.insert(0, defaultServerName)
#hostAddress = ent_destination.get()

#get the file name from the user. Default to receivedFile.jpg
lbl_getFileName = tk.Label(text="\n Enter the name the file should have at the destination")
ent_fileName = tk.Entry()
lbl_getFileName.pack()
ent_fileName.pack()

ent_fileName.insert(0, "adventuretime.jpg")

btn_confirmEntry = tk.Button(text="Transmit File", height=2, width=10)
btn_confirmEntry.pack()
btn_confirmEntry.bind('<Button-1>', sendFile)

window.mainloop() # Keeps window open until event is called or the user exits the GUI