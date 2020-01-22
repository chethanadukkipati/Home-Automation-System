import sys
file=open(sys.argv[-1],"r")
n=len(file.readlines())
file.seek(0)
import urllib
import time
import os
import shutil
import operator
starttime=[0 for i in range(n)]
totaltime=[0 for i in range(n)]
imageurl=[0 for i in range(n)]
imagesize=[0 for i in range(n)]
name=[0 for i in range(n)]
list=[0 for i in range(n)]
for i in range(n):
    starttime[i]=time.time()
    imageurl[i]=file.readline()
    name[i]="image"+str(i)
    urllib.urlretrieve(imageurl[i],name[i])
    totaltime[i]=(time.time()-starttime[i])*1000
    imagesize[i]=os.path.getsize(name[i])
for i in range(n):
    list[i]=[name[i],imageurl[i],totaltime[i],imagesize[i]]
tuple1=[(list[0]),(list[1]),(list[2])]
tuple1.sort(key=operator.itemgetter(2))
currentpath=os.getcwd()
path1='slowdownloaded'
path2='fastdownloaded'
slowpath=os.path.join(currentpath,path1)
fastpath=os.path.join(currentpath,path2)
if not os.path.exists(slowpath):
   os.makedirs(slowpath)
else:
   shutil.rmtree(slowpath)
   os.makedirs(slowpath)
if not os.path.exists(fastpath):
   os.makedirs(fastpath)
else:
    shutil.rmtree(fastpath)
    os.makedirs(fastpath)
for i in range(n//2):
    shutil.move(tuple1[i][0],fastpath)
for i in range(n//2,n):
    shutil.move(tuple1[i][0],slowpath)
print "Fast Downloaed Files"
print "URL" "," "Size(Bytes)" "," "Download Time(ms)"
for i in range(n//2):
    print tuple1[i][1],",",tuple1[i][3],",",tuple1[i][2]
print("\n")
print("----------------------------")
print("\n")
print "Slow Download Files"
print "URL" "," "Size(Bytes)" "," "Download Time(ms)"
for i in range(n//2,n):
    print tuple1[i][1],",",tuple1[i][3],",",tuple1[i][2]



