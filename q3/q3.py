import csv
import matplotlib.pyplot as plt
def q3():
    f=open("jeju_population.csv","r")
    data=csv.reader(f)
    next(data)
    row=next(data)

    year=['2013','2016','2019','2022']
    Male=[]
    Female=[]
    
    count=3
    for i in range(0,4):
        Male.append(row[count+(i*5)])
        Female.append(row[count+1+(i*5)])
    
    plt.subplots_adjust(wspace=0.4, hspace=0.7)
    plt.subplot(2,1,1)
    plt.title("Population in jeju")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.bar(year, Male, label="Male")
    for i, v in enumerate(year):
        plt.text(v,Male[i],Male[i],
                 fontsize=9,
                 horizontalalignment='center',
                 verticalalignment='bottom'
                 )
    plt.legend()

    plt.subplot(2,1,2)
    plt.title("Population in jeju")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.bar(year, Female, label="Female")
    for i, v in enumerate(year):
        plt.text(v,Female[i],Female[i],
                 fontsize=9,
                 horizontalalignment='center',
                 verticalalignment='bottom'
                 )
    plt.legend()

    plt.show()
    f.close()
    

if __name__=="__main__":
    q3()
