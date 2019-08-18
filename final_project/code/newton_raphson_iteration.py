from time import time
from numpy import linspace
from math import nan
import matplotlib
import matplotlib.pyplot as plt
import csv

def dx(f, x):
    h = 0.000000001
    d = ((f(x-(2*h)))-(8*(f(x-h)))+(8*(f(x+h)))-(f(x+(2*h))))/((12*h))
    return d

def newton_raphson_iteration(f,x,prec=10e-5,maxiter=100):
    start_time = time()
    itr = 0
    xp = []
    while(abs(f(x))>prec and itr<maxiter):
        print(f'{itr}\t{x}')
        x -= f(x)/dx(f,x)
        xp.append(x)
        itr += 1
    end_time = time()
    total_time = end_time - start_time
    return x,xp,itr,total_time

def main():
    f = lambda x: (x-3)*(x-1)*(x+1)*(x+3)
    x = -5
    z,zp,itr,time = newton_raphson_iteration(f,x)
    '''
    xlist = [-(10**i) for i in range(1,13)]
    zlist,zplist,itrlist,timelist,errorlist = [],[],[],[],[]
    for x in xlist:
        z,zp,itr,time = newton_raphson_iteration(f,x)
        zlist.append(z)
        zplist.append(zp)
        itrlist.append(itr)
        timelist.append(time)
        errorlist.append((abs((-3-z)/z))*100)

    with open('newton_table.csv',mode='w') as csv_file:
        csv_writer = csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['x=']+xlist)
        csv_writer.writerow(['root']+zlist)
        csv_writer.writerow(['iterations']+itrlist)
        csv_writer.writerow(['time']+timelist)
        csv_writer.writerow(['relative error']+errorlist)
    '''

    x = linspace(x,-x,abs(x*50))
    y = f(x)
    fp = [f(t) for t in zp]

    fig,ax = plt.subplots()
    ax.plot(x,y,zp,fp)
    ax.set(xlabel='x',ylabel='y')

    plt.legend(['f(x)','cp'])
    plt.grid()
    plt.show()

main()