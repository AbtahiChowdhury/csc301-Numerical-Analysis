from time import time
from numpy import linspace
import matplotlib
import matplotlib.pyplot as plt
import csv

def bisection(f,a,b): 
    start_time = time()
    if (f(a) * f(b) >= 0): 
        print("Invalid inputs for a and b") 
        return
    itr = 0
    c = a
    cp = []
    cp.append(c) 
    while ((b-a) >= 10e-5):
        c = (a+b)/2
        cp.append(c)
        print(f'{itr}\t{c}')
        itr += 1
        if (f(c) == 0.0): 
            break
        if (f(c)*f(a) < 0): 
            b = c 
        else: 
            a = c 
    end_time = time()
    total_time = end_time - start_time
    return c,cp,itr+1,total_time


def findPoints(f):
    a=-10000
    b=a
    for i in range(a,-a):
        if(f(a)*f(i)<0):
            b=i
    return a,b


def main():
    f = lambda x: (x-3)*(x-1)*(x+1)*(x+3)
    #alist = [-(10**i) for i in range(1,13)]
    #zlist,zplist,itrlist,timelist,errorlist = [],[],[],[],[]
    a = -5
    b = -2
    z,zp,itr,time = bisection(f,a,b)
    #a,b = findPoints(f)
    '''
    for a in alist:
        z,zp,itr,time = bisection(f,a,b)
        zlist.append(z)
        zplist.append(zp)
        itrlist.append(itr)
        timelist.append(time)
        errorlist.append((abs((-3-z)/z))*100)

    with open('bisection_table.csv',mode='w') as csv_file:
        csv_writer = csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['a=']+alist)
        csv_writer.writerow(['root']+zlist)
        csv_writer.writerow(['iterations']+itrlist)
        csv_writer.writerow(['time']+timelist)
        csv_writer.writerow(['relative error']+errorlist)
    '''
    x = linspace(a,-a,(-a)*50)
    y = f(x)
    fp = [f(t) for t in zp]

    fig,ax = plt.subplots()
    ax.plot(x,y,zp,fp)
    ax.set(xlabel='x',ylabel='y',title='Bisection Method on f(x) = (x-3)*(x-1)*(x+1)*(x+3)')

    plt.legend(['f(x)','cp'])
    plt.grid()
    plt.show()

main()