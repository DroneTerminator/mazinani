import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import statistics as s

st=0
n=0
li=[]
AKS=[]
AKS1=[]
aks=[]

for i in range (0,8):
    AKS1.append(aks)

i=Image.open('numbers/y0.5.png')
iar=np.asarray(i)
#print(iar)

for i in range(0,8):
    for j in range(0,8):
        st=sum(iar[i][j][0:3])+st
mean=st/256

#print(st,mean)

for i in iar:
    for j in i:
        st=s.mean(j[0:3])
        if st>=mean:
            st=255
           
        elif st<mean:
            st=0    
        li.append(st) 
print(li)
for i in range(0,8):
    if li[i]==0:
        AKS1[i].append([0,0,0,255])
    elif li[i]==255:
         AKS1[i].append([255,255,255,255])


AKS1=np.asarray(AKS1)
plt.imshow(AKS1)
plt.show()
#print(AKS1)
#plt.imshow(iar)
#plt.show()