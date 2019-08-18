from time import time
from numpy import linspace
import matplotlib
import matplotlib.pyplot as plt
import csv

def line_search(f,x,stepsize=0.05,prec=10e-5,maxiter=100):
    start_time = time()
    itr = 0
    xp = []
    while (abs(f(x)) > prec and itr<maxiter):
        if f(x)>0:
            xp.append(x)
            x -= stepsize
        elif f(x)<0:
            xp.append(x)
            x += stepsize
        else:
            end_time = time()
            total_time = end_time - start_time
            return x,xp,total_time
        print(f'{itr}\t{x}')
        itr += 1
    end_time = time()
    total_time = end_time - start_time
    return x,xp,itr,total_time

def main():
    xlist = [i for i in range(-5,6)]
    f = lambda x: (x-3)*(x-1)*(x+1)*(x+3)
    zlist,zplist,itrlist,timelist = [],[],[],[]

    for i in xlist:
        z,zp,itr,time = line_search(f,i)
        zlist.append(z)
        zplist.append(zp)
        itrlist.append(itr)
        timelist.append(time)

    for i in range(0,len(xlist)):
        z = zlist[i]
        zp = zplist[i]
        itr = itrlist[i]
        time = timelist[i]

        x = linspace(-5,5,500)
        y = f(x)
        fp = [f(t) for t in zp]

        fig,ax = plt.subplots()
        ax.plot(x,y,zp,fp)
        ax.set(xlabel='x',ylabel='y',title='Line Search')

        plt.legend(['f(x)','cp'])
        plt.grid()
        plt.show()

        fig,ax = plt.subplots()
        ax.plot(x,y,zp,fp)
        ax.set(xlabel='x',ylabel='y')

        plt.legend(['f(x)','cp'])
        plt.xlim(-4,4)
        plt.ylim(-20,20)
        plt.grid()
        plt.show()

main()