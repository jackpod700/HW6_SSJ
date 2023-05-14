import csv
import matplotlib.pyplot as plt

def q4():
    f=open("q4\Subway.csv",'r')
    data=csv.reader(f)
    next(data)
    next(data)
    getin_dict={}
    getout_dict={}
    total_dict={}
    for row in data:
        getin_dict[row[1]+" "+row[3]]=int(row[10])+int(row[12])
        getout_dict[row[1]+" "+row[3]]=int(row[11])+int(row[13])
        total_dict[row[1]+" "+row[3]]=getin_dict[row[1]+" "+row[3]]+getout_dict[row[1]+" "+row[3]]
    
    in_dict_list = sorted(getin_dict.items(), key=lambda x: x[1], reverse=True)
    in_b=in_dict_list[:30]
    in_x=[]
    in_y=[]
    for i in in_b:
        in_x.append(i[0])
        in_y.append(i[1])

    out_dict_list = sorted(getout_dict.items(), key=lambda x: x[1], reverse=True)
    out_b=out_dict_list[:30]
    out_x=[]
    out_y=[]
    for i in out_b:
        out_x.append(i[0])
        out_y.append(i[1])

    total_dict_list = sorted(total_dict.items(), key=lambda x: x[1], reverse=True)
    total_b=total_dict_list[:30]
    total_x=[]
    total_y=[]
    for i in total_b:
        total_x.append(i[0])
        total_y.append(i[1])
    
    plt.rc('font',family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus']=False


    plt.subplot(1,3,1)
    plt.title("출근시간 최대 승차역(30개)")
    plt.xlabel("역")
    plt.ylabel("승객 수")
    plt.bar(in_x,in_y)
    plt.xticks(fontsize=9, rotation=90)

    plt.subplot(1,3,2)
    plt.title("출근시간 하차 승차역(30개)")
    plt.xlabel("역")
    plt.ylabel("승객 수")
    plt.bar(out_x,out_y)
    plt.xticks(fontsize=9, rotation=90)

    plt.subplot(1,3,3)
    plt.title("출근시간 최대 승하차역(30개)")
    plt.xlabel("역")
    plt.ylabel("승객 수")
    plt.bar(total_x,total_y)
    plt.xticks(fontsize=9, rotation=90)
    plt.show()



if __name__=="__main__":
    q4()