import math
import csv
import time

def dx(function,x,h):
    return (function(x+h)-function(x-h))/(2*h)

def threePointMidpointFormula(function, x):
    start_time = time.time()
    h = 0.000000001
    d = ((function(x+h)-function(x-h))/(2*h))
    end_time = time.time()
    total_time = end_time - start_time
    return d, total_time

def threePointEndpointFormula(function, x):
    start_time = time.time()
    h = 0.000000001
    d = ((-3*(function(x)))+(4*(function(x+h)))-(function(x+(2*h))))/((2*h))
    end_time = time.time()
    total_time = end_time - start_time
    return d, total_time    

def fivePointMidpointFormula(function, x):
    start_time = time.time()
    h = 0.000000001
    d = ((function(x-(2*h)))-(8*(function(x-h)))+(8*(function(x+h)))-(function(x+(2*h))))/((12*h))
    end_time = time.time()
    total_time = end_time - start_time
    return d, total_time

def fivePointEndpointFormula(function, x):
    start_time = time.time()
    h = 0.000000001
    d = ((-25*(function(x)))+(48*(function(x+h)))-(36*(function(x+(2*h))))+(16*(function(x+(3*h))))-(3*function(x+(4*h))))/((12*h))
    end_time = time.time()
    total_time = end_time - start_time
    return d, total_time

def richardsonDiff(function,x): 
    start_time = time.time()
    k=9
    L=[[0.0 for i in range(0,k)] for j in range(0,k)]
    for i in range(k):
        L[i][0]=dx(function,x,1/(2**(i+1)))
    for j in range(1,k):
        for i in range(k-j):
            L[i][j]=((4**(j))*L[i+1][j-1]-L[i][j-1])/(4**(j)-1)
    end_time = time.time()
    total_time = end_time - start_time
    return L[0][k-1], total_time


def main():
    f = lambda x: math.cos(x)
    x = 1.0

    exact=-math.sin(1.0)
    richard, richardTime = richardsonDiff(f,x)
    threePointMidpoint, threePointMidpointTime = threePointMidpointFormula(f,x)
    threePointEndpoint, threePointEndpointTime = threePointEndpointFormula(f,x)
    fivePointMidpoint, fivePointMidpointTime = fivePointMidpointFormula(f,x)
    fivePointEndpoint, fivePointEndpointTime = fivePointEndpointFormula(f,x)
    

    print(f'Exact Value:     \tValue: {exact}')
    print(f'Richardson:      \tValue: {richard}\tTime: {richardTime}')
    print(f'3-point Midpoint:\tValue: {threePointMidpoint}\tTime: {threePointMidpointTime}')
    print(f'3-point Endpoint:\tValue: {threePointEndpoint}\tTime: {threePointEndpointTime}')
    print(f'5-point Midpoint:\tValue: {fivePointMidpoint}\tTime: {fivePointMidpointTime}')
    print(f'5-point Endpoint:\tValue: {fivePointEndpoint}\tTime: {fivePointEndpointTime}')
    
    
    values = [threePointEndpoint, threePointMidpoint, fivePointEndpoint, fivePointMidpoint, richard]
    exactValues = [exact for i in range(len(values))]
    times = [threePointEndpointTime, threePointMidpointTime, fivePointEndpointTime, fivePointMidpointTime, richardTime]
    absoluteError = [(exact-i) for i in values]
    relativeError = [((abs((exact-i)/(i)))*100) for i in values]

    with open ('diff_data.csv',mode='w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['','3-point Endpoint','3-point Midpoint','5-point Endpoint','5-point Midpoint','Richard Extrapolation'])
        csv_writer.writerow(['Values']+values)
        csv_writer.writerow(['Exact Value']+exactValues)
        csv_writer.writerow(['Times']+times)
        csv_writer.writerow(['Absolute Error']+absoluteError)
        csv_writer.writerow(['Relative Error']+relativeError)

main()