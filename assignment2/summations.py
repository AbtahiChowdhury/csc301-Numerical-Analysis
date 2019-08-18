import math
import time
import csv
#import matplotlib.pyplot as plt

def naiveSum(n):
    start_time=time.time()
    s=0
    for i in range(0,n):
        s += math.pi
    end_time=time.time()
    totaltime=end_time-start_time
    return s, totaltime

def compensatedSum(n):
    start_time=time.time()
    s=0
    e=0
    for i in range(0,n):
        temp=s
        y=math.pi+e
        s=temp+y
        e=(temp-s)+y
    s += e
    end_time=time.time()
    totaltime=end_time - start_time
    return s, totaltime

def main():
    N=[10**i for i in range(6,10)]
    #N=[10**i for i in range(6,8)]

    naivesums=[]
    naivesumtimes=[]

    compensatedsums=[]
    compensatedsumtimes=[]

    exactsums=[]
    for n in N:
        naivesum, naivesumtime = naiveSum(n)
        naivesums.append(naivesum)
        naivesumtimes.append(naivesumtime)

        compensatedsum, compensatedsumtime = compensatedSum(n)
        compensatedsums.append(compensatedsum)
        compensatedsumtimes.append(compensatedsumtime)

        exactsums.append(n * math.pi)

    '''
    for i in range(0,4):
        print(f'N={N[i]} \n\nNaive Summation \nSum={naivesums[i]} \nExact Sum={exactsums[i]} \nTime={naivesumtimes[i]} \n\nCompensated Summation \nSum={compensatedsums[i]} \nExact Sum={exactsums[i]} \nTime={compensatedsumtimes[i]}\n\n')
    '''
    with open ('data.csv',mode='w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['','10^6','10^7','10^8','10^9'])
        csv_writer.writerow(['Naive Sum']+naivesums)
        csv_writer.writerow(['Naive Time']+naivesumtimes)
        csv_writer.writerow(['Compensated Sum']+compensatedsums)
        csv_writer.writerow(['Compensated Time']+compensatedsumtimes)
        csv_writer.writerow(['Exact Value']+exactsums)

    '''
    data = [naivesums,naivesumtimes,compensatedsums,compensatedsumtimes,exactsums]
    rowlabel=('Native Sum','Native Time','Compensated Sum','Compensated Time','Exact Value')
    collabel=('10^6','10^7','10^8','10^9')
    
    fig, axs = plt.subplots()
    axs.axis('off')
    axs.table(cellText=data, rowLabels=rowlabel, colLabels=collabel, cellLoc='center', loc='center')
    plt.show()
    '''
main()