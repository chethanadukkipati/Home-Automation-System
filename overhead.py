def overhead():
    import os
    from subprocess import call
    print("Capturing network traffic")
    call(["tshark","-c","500","-w","/home/pi/net.txt"])
    print("Extracting fields:")
    call(["tshark","-r","/home/pi/net.txt","-T","fields","-e","frame.number","-e"
         ,"frame.time_relative","-e","ip.src","-e","ip.dst",
          "-E","header=y","-E","quote=n","-E","occurrence=f"])
    print("Packets from thepi:")
    call(["tshark","-r","/home/pi/net.txt","-R","ip.src==10.0.0.103"])
    print("Http packets in the stored file")
    call(["tshark","-q","-r","/home/pi/net.txt","-Y","http","-z","http,tree"])
    #print("Tcp packets in the stored file")
    #call(["tshark","-q","-r","/home/pi/net.txt","-Y","tcp","-z","http,tree"])
    call(["bmon"])

    
