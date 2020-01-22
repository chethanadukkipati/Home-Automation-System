def function22():
    import socket
    import os
    s=socket.socket()
    host="54.173.44.219"
    port=20000
    auth_status="NA"
    while(1):
        s.connect((host,port))
        print "Waiting for auth file"
        received=s.recv(100)
        print received
        return received
        print "got it"
        break;
        s.close()
    
