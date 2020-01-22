def function4():
    import os  
    from subprocess import call
    x=1
    while(x):
        try:
            call(["scp","-i","/home/pi/projectCN_east.pem","ec2-user@ec2-54-173-44-219.compute-1.amazonaws.com:/home/ec2-user/authstatus.txt","/home/pi/authstatus.txt"])
            if(os.path.exists("/home/pi/authstatus.txt")):
               break
        except:
            x=1

