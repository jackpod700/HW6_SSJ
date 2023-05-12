import csv
import matplotlib.pyplot as plt
def q1():
    korea_f=open('korea.csv', 'r',encoding="ANSI")
    seoul_f=open('seoul.csv','r',encoding="ANSI")
    daejeon_f=open('daejeon.csv','r',encoding="ANSI")
    busan_f=open('busan.csv','r',encoding="ANSI")
    jeju_f=open('jeju.csv','r',encoding="ANSI")

    korea=readdata(korea_f)
    seoul=readdata(seoul_f)
    daejeon=readdata(daejeon_f)
    busan=readdata(busan_f)
    jeju=readdata(jeju_f)

    plt.title("Average Temperature in korea")
    plt.plot(korea, label="Korea")
    plt.plot(seoul, label="seoul")
    plt.plot(daejeon, label="daejeon")
    plt.plot(busan, label="busan")
    plt.plot(jeju, label="jeju")
    plt.xlabel("Month")
    plt.ylabel("Celsius")
    plt.legend()
    plt.show()
    
    korea_f.close()
    seoul_f.close()
    daejeon_f.close()
    busan_f.close()
    jeju_f.close()
    

def readdata(f):
    list=[]
    data = csv.reader(f)
    next(data)
    for row in data:
        list.append(float(row[2]))
    return list

if __name__=="__main__":
    q1()
