def function3(number):
    from subprocess import call
    call(["chmod","400","/home/pi/projectCN_east.pem"])
    call(["scp","-i","/home/pi/projectCN_east.pem","/home/pi/resultfile.txt","ec2-user@ec2-54-173-44-219.compute-1.amazonaws.com:~"])
    for i in range(1,number):
        call(["scp","-i","/home/pi/projectCN_east.pem",("/home/pi/testimage%d.jpg"%i),"ec2-user@ec2-54-173-44-219.compute-1.amazonaws.com:~"])
    
