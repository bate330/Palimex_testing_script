import socket,sys,time

class Cmds:

    def __CreateSocket(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, port))
        except:
            print("No Connection with printer")
        return s

    def __SendData(self, socket, cmd):
        socket.sendall(cmd.encode())

    #use for stop printing
    def StopPrint(self, host, port):
        s = self.__CreateSocket(host, port)
        try:
            self.__SendData(s, '{"CMD":31}')
        except:
            print("Cannot send Cmd (Stop Print)")
        print("Printing has Stopped")
        s.close()
        time.sleep(0.1)

    #use for start printing
    def StartPrint(self, host, port):
        s = self.__CreateSocket(host, port)
        try:
            self.__SendData(s, '{"CMD":30,"ForcePrint":1}')
        except:
            print("Cannot send Cmd (Start Print)")
        s.close()
        time.sleep(0.1)

