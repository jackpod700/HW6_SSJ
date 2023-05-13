import random
def q2_1():
    f=open("dice.csv","w")
    dice(100,f)
    dice(1000,f)
    dice(10000,f)
    dice(100000,f)
        
    f.close()
    print("complete")
    
def dice(n,f):
    f.write("Dice Roll "+str(n)+"\n")
    i=0
    while(i<n):
        if(i==n-1):
            f.write(str(random.randrange(1,7))+"\n")
            i+=1
        else:
            f.write(str(random.randrange(1,7))+",")
            i+=1
    
    
if __name__=="__main__":
    q2_1()