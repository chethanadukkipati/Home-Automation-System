#def function21():
from subprocess import call
#name =input("enter name of the person you want to add:")
for i in range(1,11):
     call(["fswebcam",("/home/pi/image%d.jpg"%i)])
     call(["python","add_image.py","-i",("/home/pi/image%d.jpg"%i),"-c","'home'","-l",'tom'])
