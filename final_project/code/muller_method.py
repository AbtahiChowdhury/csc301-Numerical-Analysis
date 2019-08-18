from time import time
from numpy import linspace
from cmath import sqrt
import matplotlib
import matplotlib.pyplot as plt
import csv
import math

def muller_method(f,x0,x1,x2,prec=10e-5,maxiter=100):
    start_time = time()
    itr = 0
    xp = []
    while(itr<maxiter):
        fx0 = f(x0)
        fx1 = f(x1)
        fx2 = f(x2)

        u = x0-x2
        v = x1-x2
        y = fx0-fx2
        z = fx1-fx2

        try:
            a = ((u*z)-(y*v))/(u*v*(v-u))
            b = ((y*v*v)-(u*u*z))/(v*((u*v)-(u*u)))
            c = fx2
        except ZeroDivisionError:
            end_time = time()
            total_time = end_time - start_time
            return math.nan,[],itr,total_time

        denominator_plus = b + sqrt((b*b)-(4*a*c))
        denominator_minus = b - sqrt((b*b)-(4*a*c))
        numerator = -2*c

        if(abs(denominator_minus) >= abs(denominator_plus)):
            x3 = x2 + ((numerator)/(denominator_minus))
        else:
            x3 = x2 + ((numerator)/(denominator_plus))
        
        print(f'{itr}: {x3}')
        xp.append(x3)

        if(abs((x3-x2)/x2) < prec):
            break
        
        x0,x1,x2 = x1,x2,x3
        itr += 1
    end_time = time()
    total_time = end_time - start_time
    return x3,xp,itr,total_time

def main():
    X0 = [-(10**i) for i in range(1,13)]
    X2 = [10**i for i in range(1,13)]

    f = lambda x: (x-3)*(x-1)*(x+1)*(x+3)
    #x0 = 0
    #x1 = 0
    #x2 = 0
    guesses,zlist,zplist,itrlist,timelist,errorlist = [],[],[],[],[],[]
    for i in range(0,12):
        if(X0[i] != X2[i]):
            z,zp,itr,time = muller_method(f,X0[i],0,X2[i])                    
            guesses.append(tuple((X0[i],0,X2[i])))
            zlist.append(z)
            zplist.append(zp)
            itrlist.append(itr)
            timelist.append(time)
            errorlist.append((abs((1-z.real)/z.real))*100)
    with open('muller_table.csv',mode='w') as csv_file:
        csv_writer = csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['guesses']+guesses)
        csv_writer.writerow(['root']+zlist)
        csv_writer.writerow(['iterations']+itrlist)
        csv_writer.writerow(['time']+timelist)
        csv_writer.writerow(['relative error']+errorlist)

    '''
    f = lambda x: (x**4) + (x**2) + 5
    x0 = -1
    x1 = 0
    x2 = 1
    '''
    '''
    z,zp,itr,time = muller_method(f,x0,x1,x2)
    zpreal = [t.real for t in zp]
    zpimag = [t.imag for t in zp]
    print(z)
    
    x = linspace(-5,5,50*10)
    y = f(x)
    fp = [f(t.real) for t in zp]

    fig,ax = plt.subplots()
    ax.plot(x,y,zp,fp)
    ax.set(xlabel='x',ylabel='y')

    plt.legend(['f(x)','cp'])
    plt.grid()
    plt.show() 

    fig,ax = plt.subplots()
    ax.plot(zpreal,zpimag)
    i = 0
    for xy in zip(zpreal,zpimag):
        ax.annotate('%s' % i, xy=xy, textcoords='data')
        i +=1
    ax.set(xlabel='real',ylabel='imag')

    plt.grid()
    plt.show()    
    '''

main()