import os
import sys
bytessend=0
sys.path.insert(0,"/home/pi")
number=input("Enter number of frames for authentication:");
for i in range(1,number+1):
    from subprocess import call
    call(["fswebcam", ("/home/pi/testimage%d.jpg"%i)])
#sys.path.insert(0,"/home/pi/VL53L0X_rasp_python/python")
from VL53L0X_example import *
measured_distance=function2()
print(measured_distance)
sys.path.insert(0,"/home/pi/pi-detector/scripts")
method=input("Enter 1.AWS 2.Opencv")
if (method==1):
   import facematch
   result, name=facematch.main()
if (method==2):
    import training
    result,name=training.function20()
if(result=="Identity Matched"):
    import distancecompare
    output=distancecompare.function6(name,60)
    print output
    if(output==1):
        import details
        print name
        profession,relation,age=details.function5(name)
        print profession
        fi=open("/home/pi/resultfile.txt","r+")
        fi.write(name)
        fi.write(",")
        fi.write(str(measured_distance))
        fi.write(",")
        fi.write(profession)
        fi.write(",")
        fi.write(relation)
        fi.write(",")
        fi.write(str(age))
        fi.close()
        import serverupload
        serverupload.function3(number)
        t=input("1. pooling 2. Non-pooling")
        if(t==1):
            import serverdownload
            serverdownload.function4()
            f=open("/home/pi/authstatus.txt","r")
            text=f.read()
            bytessend=bytessend+len(text)
            print text
            print("\n")
            print("Number of bytes send in entire travel for authorization command:")
            print(bytessend)
        if(t==2):
            import nopool
            text=nopool.function22()
            
        import convert
        final=convert.function16(name)
        print final
        import audio
        if(text=="Authentication Successfull"):
            wordtext="Welcome home:"+name
            audio.function8(wordtext)
        else:
            wordtext="Authentication failed...Please try again"
            audio.function8(wordtext)
    else:
         print("Distance not matched with the define limits:")
         print("Try again....")
    
elif(result=="No face matches detected"):
    print ('No face matched with the databasd')
else:
   print ("No face detetcted:Try again")
extra=input("Wanna enter new user press 1:")
if(extra==1):
    import newuser
    newuser.function21()
import overhead
overhead.overhead()

   
    
   


   







