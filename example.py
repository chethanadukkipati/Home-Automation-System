 import io
import socket
import os
import time
serverPort=20000
host=socket.gethostname()
print host
s=socket.socket()
s.bind((host,serverPort))
s.listen(5)
bytessend=0
bytessendimage=0
print('server ready to receive')
while 1:
    connectionSocket1,addr=s.accept()
    for i in range(0,10):
        print "Waiting for server to reply"
        if(i!=0):
          print "sending 0"
connectionSocket5.send("0")
        connectionSocket,addr=s.accept()
        print('Reading the image'+str(i))
        with open('testimage'+str(i+1)+'.jpg','rb') as testimg:
            jpgdata=testimg.read()
            bytessendimage=bytessendimage+len(jpgdata)
            connectionSocket.send(jpgdata)
        testimg.close()
        connectionSocket.close()
        if(i!=8):
          print i
          connectionSocket5,addr=s.accept()
          print "Got connection for wait"
          connectionSocket5.send("1")
          print "Sending 1"
    connectionSocket.close()
    connectionSocket5.close()
    connectionSocket2,addr=s.accept()
    print("Reading image details")
    with open('resultfile.txt','r') as testdata:
        data=testdata.read()
        connectionSocket2.send(data)
    testdata.close()
    connectionSocket2.close()
    connectionSocket3,addr=s.accept()
    print("Authentication Status")
    with open('authstatus.txt','w') as status:
        inputdata=connectionSocket3.recv(100)
        bytessend=bytessend+len(inputdata)
        print inputdata
        if(inputdata=="1"):
            status.write("Authentication Successfull")
        else:
            status.write("Authentication Failed:")
    status.close()
    connectionSocket3.close()
    f=open('authstatus.txt','r')
    auth_status=f.read()
    connectionSocket1.send(auth_status)
    connectionSocket1.close()
    print "Total number of bytes send from pi to server and from server to android and reverse direction for 1 cycle"
    print (bytessendimage*2)
