import random
import csv
import matplotlib.pyplot as plt
def q2_2():
    f=open('dice.csv','r')
    data = csv.reader(f)
    
    y=[]
    case=[100,1000,10000,100000]
    casecount=0
    for row in data:
        i=0
        while(i<len(row)):
            if 'Dice' in row[0]:
                y=[]
                break
            if i==len(row)-1:
                y.append(int(row[i]))
                plt.subplot(2,2,casecount+1)
                plt.subplots_adjust(wspace=0.4, hspace=0.7)
                plt.hist(y, bins=range(1,8),color="red", align="left",rwidth=0.5)
                plt.title("Dice roll "+str(case[casecount])+" Times")
                plt.xlabel("Dice Number")
                plt.ylabel("Times")
                plt.xticks(range(1,7))
                casecount+=1
            y.append(int(row[i]))
            i+=1
    plt.show()
    f.close()

if __name__=="__main__":
    q2_2()