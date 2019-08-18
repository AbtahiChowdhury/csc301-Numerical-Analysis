from time import time
from numpy import linspace
import matplotlib
import matplotlib.pyplot as plt

def inverse_quadratic_interpolation(f,x0,x1,x2,prec=10e-5,maxiter=100):
    start_time = time()
    itr = 0
    xp = []
    while(abs(x1-x0)>prec and itr<maxiter):
        fx0 = f(x0)
        fx1 = f(x1)
        fx2 = f(x2)
        L0 = (x0*fx1*fx2)/((fx0-fx1)*(fx0-fx2))
        L1 = (x1*fx0*fx2)/((fx1-fx0)*(fx1-fx2))
        L2 = (x2*fx1*fx0)/((fx2-fx0)*(fx2-fx1))
        new = L0+L1+L2
        x0,x1,x2 = new,x0,x1
        print(f'{itr}\t{new}')
        xp.append(new)
        itr += 1
    end_time = time()
    total_time = end_time - start_time
    return x0,xp,itr,total_time

def main():
    f = lambda x: (x-3)*(x-1)*(x+1)*(x+3)
    x0 = -8
    x1 = -5
    x2 = -9
    z,zp,itr,time = inverse_quadratic_interpolation(f,x0,x1,x2)
    print(z)

    x = linspace(-5,5,500)
    y = f(x)
    fp = [f(t) for t in zp]

    fig,ax = plt.subplots()
    ax.plot(x,y,zp,fp)
    ax.set(xlabel='x',ylabel='y')

    plt.legend(['f(x)','cp'])
    plt.grid()
    plt.show()    

main()