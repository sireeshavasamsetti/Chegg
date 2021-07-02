#The materials in the transport company are loaded with materials of different weights. The program calculates how many materials and how many total materials are loaded when the truck is full.
#The program stops when -1 is entered.
a=[]
i=0
sum1=0
while(True):
    i=i+1
    print("Enter "+str(i)+". weight of the material",end=":")
    s=int(input())
    
    if(s==(-1)):
       break
    else:
       a.append(s)
       sum1+=s
     

print(len(a)," Materials Loaded on Truck")
print("Total Weight of Materials:",sum1)
print("Programming language is python. Thank you for your efforth and knowledge")