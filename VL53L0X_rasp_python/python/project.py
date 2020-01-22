import os
import sys
sys.path.insert(0,"/home/pi")
from subprocess import call
call(["fswebcam", "/home/pi/testimage.jpg"])
#sys.path.insert(0,"/home/pi/VL53L0X_rasp_python/python")
from VL53L0X_example import *
measured_distance=function2()
print(measured_distance)
sys.path.insert(0,"/home/pi/pi-detector/scripts")
import facematch
result, name=facematch.main()
if(result=="Identity Matched"):
    import distancecompare
    output=distancecompare.function6(name,measured_distance)
    print output
    if(output==1):
        import details
        print name
        profession,relation,age=details.function5(name)
        print profession
        fi=open("resultfile.txt","r+")
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
        serverupload.function3()
        import serverdownload
        serverdownload.function4()
        import audio
        f=open("/home/pi/authstatus.txt","r")
        text=f.read()
        print text
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

   
    
   


   

#call(["python","/home/pi/VL53L0X_rasp_python/python/VL53L0X_example.py"])

#call(["python","/home/pi/pi-detector/scripts/facematch.py","-i","/home/pi/testimage.jpg","-c","home"])





