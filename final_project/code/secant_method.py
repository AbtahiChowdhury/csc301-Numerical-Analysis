from time import time
from numpy import linspace
import matplotlib
import matplotlib.pyplot as plt

def secant(f,x0,x1,prec=10e-5,maxiter=100):
    start_time = time()
    itr = 0
    xp = []
    while(abs(x1-x0)>prec and itr<maxiter):
        x2 = x1 - ((f(x1)*(x1-x0))/(f(x1)-f(x0)))
        x1,x0 = x2,x1
        xp.append(x2)
        print(f'{itr}\t{x2}')
        itr += 1
    end_time = time()
    total_time = end_time - start_time
    return x2,xp,itr,total_time


def main():
    f = lambda x: (x-3)*(x-1)*(x+1)*(x+3)
    x0 = -10
    x1 = -2
    z,zp,itr,time = secant(f,x0,x1)
    print(z)

    x = linspace(-5,5,500)
    y = f(x)
    fp = [f(t) for t in zp]

    fig,ax = plt.subplots()
    ax.plot(x,y,zp,fp)
    ax.set(xlabel='x',ylabel='y')

    plt.legend(['f(x)','cp'])
    plt.xlim(-5,5)
    plt.ylim(-20,15)
    plt.grid()
    plt.show()

main()