import math
import time
import csv

def trapezoidalRule(function,a,b):
    start_time = time.time()
    h = b-a
    x0 = a
    x1 = b
    d = (h/2)*(function(x0)+function(x1))
    end_time = time.time()
    total_time = end_time - start_time
    return d, total_time

def simpsonRule(function,a,b):
    start_time = time.time()
    h = (b-a)/2
    x0 = a
    x1 = a+h
    x2 = b
    d = (h/3)*(function(x0)+(4*function(x1))+function(x2))
    end_time = time.time()
    total_time = end_time - start_time
    return d, total_time

def newtonCotesN4(function,a,b):
    start_time = time.time()
    h = (b-a)/4
    x0 = a
    x1 = a+h
    x2 = x1+h
    x3 = x2+h
    x4 = b
    d = ((2*h)/45)*((7*function(x0))+(32*function(x1))+(12*function(x2))+(32*function(x3))+(7*function(x4)))
    end_time = time.time()
    total_time = end_time - start_time
    return d, total_time

def compositeSimpsonRule(function,a,b):
    start_time = time.time()
    n = 1000000
    h = (b-a)/n
    x = [a+(j*h) for j in range(0,n+1)]
    secondterm = 0
    for j in range(1,int(n/2)):
        secondterm += function(x[(2*j)-1])
    thirdterm = 0
    for j in range(1,int(n/2)+1):
        thirdterm += function(x[2*j])
    d = (h/3)*((function(a))+(2*secondterm)+(4*thirdterm)+(function(b)))
    end_time = time.time()
    total_time = end_time - start_time
    return d, total_time

def compositeTrapezoidalRule(function,a,b):
    start_time = time.time()
    n = 1000000
    h = (b-a)/n
    x = [a+(j*h) for j in range(0,n+1)]
    secondterm = 0
    for j in range(1,n):
        secondterm += function(x[j])
    d = (h/2)*((function(a))+(2*secondterm)+(function(b)))
    end_time = time.time()
    total_time = end_time - start_time
    return d, total_time

def compositeMidpointRule(function,a,b):
    start_time = time.time()
    n = 1000000
    h = (b-a)/n
    x = [a+(j*h) for j in range(0,n+1)]
    secondterm = 0
    for j in range(2,int(n/2)+1):
        secondterm += function(x[2*j])
    d = (2*h)*(secondterm)
    end_time = time.time()
    total_time = end_time - start_time
    return d, total_time

def S(function,a,b):
    h = (b-a)/2
    return ((h/3)*(function(a)+(4*function(a+h))+function(b)))


def adaptiveQuadrature(function,a,b):
    start_time = time.time()
    firstterm = S(function,a,((a+b)/2))
    secondterm = S(function,((a+b)/2),b)
    thirdterm = (1/16)*((16/15)*((S(function,a,b))-(S(function,a,((a+b)/2)))-(S(function,((a+b)/2),b))))
    d = firstterm+secondterm-thirdterm
    end_time = time.time()
    total_time = end_time - start_time
    return d, total_time


def main():
    f = lambda x: math.sin(x) + math.cos(x)
    a = 0.4
    b = 1.6
    exact = (math.sin(1.6)-math.cos(1.6))-(math.sin(0.4)-math.cos(0.4))
    trapezoidalrule, trapezoidalruletime = trapezoidalRule(f,a,b)
    simpsonrule, simpsonruletime = simpsonRule(f,a,b)
    newtoncotesn4, newtoncotesn4time = newtonCotesN4(f,a,b)
    compositetrapezoidal, compositetrapezoidaltime = compositeTrapezoidalRule(f,a,b)
    compositesimpson, compositesimpsontime = compositeSimpsonRule(f,a,b)
    compositemidpointrule, compositemidpointruletime = compositeMidpointRule(f,a,b)
    adaptivequadrature, adaptivequadraturetime = adaptiveQuadrature(f,a,b)
    print(f"Trapezoidal        \t{trapezoidalrule}\t{trapezoidalruletime}")
    print(f"Simpson            \t{simpsonrule}\t{simpsonruletime}")
    print(f"Newton Cotes N=4   \t{newtoncotesn4}\t{newtoncotesn4time}")
    print(f"Composite Midpoint \t{compositemidpointrule}\t{compositemidpointruletime}")
    print(f"Composite Simpson  \t{compositesimpson}\t{compositesimpsontime}")
    print(f"Composite Trapezoid\t{compositetrapezoidal}\t{compositetrapezoidaltime}")
    print(f"Adaptive Quadrature\t{adaptivequadrature}\t{adaptivequadraturetime}")
    print(f"Exact              \t{exact}")

    values = [trapezoidalrule, simpsonrule, newtoncotesn4, compositetrapezoidal, compositemidpointrule, compositesimpson, adaptivequadrature]
    exactValues = [exact for i in range(len(values))]
    times = [trapezoidalruletime, simpsonruletime, newtoncotesn4time, compositetrapezoidaltime, compositemidpointruletime, compositesimpsontime, adaptivequadraturetime]
    absoluteError = [(exact-i) for i in values]
    relativeError = [((abs((exact-i)/(i)))*100) for i in values]

    with open ('integral_data.csv',mode='w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['','Trapezoidal Rule','Simpson Rule','Newton Cotes N=4','Composite Trapezoidal Rule','Composite Midpoint Rule','Composite Simpson Rule','Adaptive Quadrature'])
        csv_writer.writerow(['Values']+values)
        csv_writer.writerow(['Exact Value']+exactValues)
        csv_writer.writerow(['Times']+times)
        csv_writer.writerow(['Absolute Error']+absoluteError)
        csv_writer.writerow(['Relative Error']+relativeError)

    

main()