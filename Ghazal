import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt
import statistics as stat 
i = Image.open('images/numbers/y0.5.png')
iar=np.asarray(i)
li=[]
list(iar)
print(list(iar))
print(iar)
plt.imshow(iar)
plt.show()
def threshold():
    balanceAr=[]
    for i in iar:
        for j in i:
            avgnum=stat.mean(j[:3])
            balanceAr.append(avgnum)
            balance=stat.mean(balanceAr)
    
    for i in iar:
        for j in i:
            if avgnum>balance:
                j[0]=0
                j[1]=0
                j[2]=0
                j[3]=0
            else:
                j[0]=0
                j[1]=255
                j[2]=255
                j[3]=255
    return iar
threshold()
