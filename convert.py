def function16(name):
    import urllib2
    import speech_recognition as sr
    from subprocess import call
#from converter import Converter
    import os
    #file=input("Enter wav file path and name")
#c=Converter()
#call(["avconv","-i","/home/pi/voice.mp3","-vn","-f","wav","voice.wav"])
    r=sr.Recognizer()
    if(name=='chethana'):
        with sr.WavFile('/home/pi/person1.wav') as source:
            audio=r.record(source)
    elif(name=='dinesh'):
        with sr.WavFile('/home/pi/dinesh.wav') as source:
            audio=r.record(source)
    elif(name=='sampu'):
        with sr.WavFile('/home/pi/sampu.wav') as source:
            audio=r.record(source)
    command=r.recognize_google(audio)
    print command
    if(name=='chethana'and command=='hello home'):
        return "successfull"
    elif(name=='dinesh' and command=='happy'):
        return "successfull"
    elif(name=='sampu'and command=='crazy'):
        return "successfull"
    else:
        return "failed"
         
