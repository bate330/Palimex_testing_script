import socket, time
from Cmds import Cmds

#Function to send code to printer
def SendCode(host, port, code):
    code = code + '\r'  #add end marker 1 byte '0D'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #Create socket
    try:
        s.connect((host, port)) #connect to created socket
    except:
        print("No Connection with printer")
    try:
        print(code)
        s.sendall(code.encode())    #Send Code to printer
    except:
        print("Cannot send Cmd")
    data = s.recv(1024) #Get answer data from printer, we may somehow use this information

    #In this case we are waiting for photocell signal, which send data from printer,
    # after that, we will go to the next step

    s.close()   #close socket
    print("printed!")
    time.sleep(0.1) #we have to use time sleep

#Set printer settings
host = "192.168.100.2"  #Printer's IP address
port_codes = 5001   #Printer's port to send data to print selected project
port_cmds = 3121    #Printer's port to send control commands
project_name = 'test_palimex.prj'   #created project in printer library

cmds = Cmds()   #create object of Cmd's Class to use function from there

#Remotely start printing
cmds.StartPrint(host, port_cmds)

#send codes from code list to printer
codes = ["3p4.eu/XNHXM37C6", "3p4.eu/F49FJRP98", "3p4.eu/4KF95DXXF", "3p4.eu/192JG0JXI", "3p4.eu/QODPGGHIU"]    #code list
while 1:    #endless loop
    for code in codes:
        SendCode(host, port_codes, code) #send code in loop

#We can also Remotely stop printing: cmds.StopPrint(host, port_cmds)