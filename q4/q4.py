import csv
import matplotlib.pyplot as plt

def q4():
    f=open("Subway.csv",'r')
    data=csv.reader(f)
    next(data)
    next(data)
    print("done")



if __name__=="__main__":
    q4()