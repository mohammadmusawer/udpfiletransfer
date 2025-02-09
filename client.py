#This is the client side of a client/server pair. It sends an image to the server in 1024kb packets
#It has a basic gui to gather information from the user
#Network Design. Prof Vokkarane
#Due 9/30/20
#Submitted 9/30/20
#By: Julie Dawley, Mohammad Musawer, and Ricardo Candanedo

import socket
import tkinter as tk
import time

def transmitFile(hostAddress, fileName):
    # function to transmit the file. Contains the code copy/pasted from phase1
    # takes as input the host address to send the file to and the name for the file upon arrival

    # initialization of the object and connects it to the port and host address
    socketVar = socket.socket()
    port = 8090
    socketVar.connect((hostAddress, port))

    # open file in read-binary
    fileToSend = open(fileName, 'rb')

    # finds the length of the file, calculates the number of packets and prints all info
    fileToSend.seek(0, 2)
    fileLength = fileToSend.tell()
    numOfPackets = int(fileLength / 1024) + 1
    fileToSend.seek(0, 0)
    print(fileLength)
    print(fileName)
    print(numOfPackets)

    # encodes the fileName and numOfPackets and sends it to the server
    encodedFileName = fileName.encode()
    socketVar.send(encodedFileName)
    time.sleep(1) # delays by 1 second
    stringNumOfPackets = str(numOfPackets)
    encodedStringNumOfPackets = stringNumOfPackets.encode()
    socketVar.send(encodedStringNumOfPackets)

    # loop to keep sending packets and prints the packet number that is being sent
    for x in range(1, numOfPackets + 1):
        numOfPacketsSend_String = f"Sending packet #{x} the server..."
        print(numOfPacketsSend_String)
        data = fileToSend.read(1024)
        socketVar.send(data)
    fileToSend.close()

    # displays that the data has been sent successfully
    print("\nData has been sent successfully!")

    return

def closeProgram(event):
    #closes the program
    window.quit()
    return

def sendFile(event):
    # event to send the file once the user has clicked the "Send file" button
    hostAddress = ent_destination.get()
    fileName = ent_fileName.get()
    print(fileName)

    #close the window and send the file
    window.destroy()
    transmitFile(hostAddress, fileName)

    #Display the confirmation the file sent
    lbl_FileSent = tk.Label(text="The file has been sent.")
    lbl_FileSent.pack()

    btn_confirmExit = tk.Button(text="Click to exit.", width=16, height=2)
    btn_confirmExit.pack()
    btn_confirmExit.bind('<Button-1>', closeProgram)

    return

# get the name of this machine to use as a default address
defaultServerName = socket.gethostname()
window = tk.Tk()

# introductory message
lbl_introduction = tk.Label(text = "Networking Design Project Phase 2. \n"
                             "EECE.4830 201. Professor Vokkarane. \n"
                             "By: Julie Dawley, Ricardo Candanedo, and Mohammad Musawer \n \n"
                             "Destination Computer: Defaults to this machine. \n"
                             "Change to the address in serverClient if running client and server on seperate machines")
lbl_introduction.pack()

# get the destination name from the user, default to defaultServerName
ent_destination = tk.Entry()
ent_destination.pack()
ent_destination.insert(0, defaultServerName)

# get the file name from the user. Default to adventuretime.jpg
lbl_getFileName = tk.Label(text="\n Enter the name the file should have at the destination")
ent_fileName = tk.Entry()
lbl_getFileName.pack()
ent_fileName.pack()
ent_fileName.insert(0, "adventuretime.jpg")

#button to transmit the file
btn_confirmEntry = tk.Button(text="Transmit File", height=2, width=10)
btn_confirmEntry.pack()
btn_confirmEntry.bind('<Button-1>', sendFile)

window.mainloop()  #GUI loop