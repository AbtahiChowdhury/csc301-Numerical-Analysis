import math
import time
import csv
from decimal import Decimal

def taylorSin(x,n):
    start_time = time.time()
    s = 0
    for k in range(0,n+1):
        s += (Decimal(((-1)**k))*(Decimal((x**((2*k)+1)))/(Decimal(math.factorial((2*k)+1)))))
    end_time = time.time()
    total_time = end_time - start_time
    s = float(s)
    return s, total_time

def main():
    X=[0.03125,0.0625,0.125,0.25,0.5,1,2,4]
    N=[1,2,3,4,8,16,32,64,128,256]
    taylorSins=[[0.0 for i in range(len(X))] for j in range(len(N))]
    taylorSinTimes=[[0.0 for i in range(len(X))] for j in range(len(N))]
    sinExactValues=[math.sin(x) for x in X]

    for i in range(len(N)):
        for j in range(len(X)):
            taylorsin, taylorsintime = taylorSin(X[j],N[i])
            taylorSins[i][j] = taylorsin
            taylorSinTimes[i][j] = taylorsintime
        
    for i in range(len(X)):
        for j in range(len(N)):
            if (X[i] <= 0.0625):
                print(f'x={X[i]}\tn={N[j]}\t     sin(x)={taylorSins[j][i]}\t\ttime={taylorSinTimes[j][i]}')
            else:
                print(f'x={X[i]}\t\tn={N[j]}\t     sin(x)={taylorSins[j][i]}\t\ttime={taylorSinTimes[j][i]}')
        if (X[i] <= 0.0625):
            print(f'x={X[i]}\t\tExact Value={sinExactValues[i]}\n')
        else:
            print(f'x={X[i]}\t\t\tExact Value={sinExactValues[i]}\n')

    taylorSinAbsoluteErrors=[[0.0 for i in range(len(X))] for j in range(len(N))]
    taylorSinRelativeErrors=[[0.0 for i in range(len(X))] for j in range(len(N))]
    for i in range(len(N)):
        for j in range(len(X)):
            taylorSinAbsoluteErrors[i][j]=((sinExactValues[j])-(taylorSins[i][j]))
            taylorSinRelativeErrors[i][j]=abs(((taylorSinAbsoluteErrors[i][j])/(taylorSins[i][j]))*100)

    with open ('taylor_sin_data.csv',mode='w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['','x=1/32','x=1/16','x=1/8','x=1/4','x=1/2','x=1','x=2','x=4'])
        csv_writer.writerow(['n=1']+taylorSins[0])
        csv_writer.writerow(['n=2']+taylorSins[1])
        csv_writer.writerow(['n=3']+taylorSins[2])
        csv_writer.writerow(['n=4']+taylorSins[3])
        csv_writer.writerow(['n=8']+taylorSins[4])
        csv_writer.writerow(['n=16']+taylorSins[5])
        csv_writer.writerow(['n=32']+taylorSins[6])
        csv_writer.writerow(['n=64']+taylorSins[7])
        csv_writer.writerow(['n=128']+taylorSins[8])
        csv_writer.writerow(['n=256']+taylorSins[9])
        csv_writer.writerow(['Exact Value']+sinExactValues)
    
    with open ('taylor_sin_time_data.csv',mode='w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['','x=1/32','x=1/16','x=1/8','x=1/4','x=1/2','x=1','x=2','x=4'])
        csv_writer.writerow(['n=1']+taylorSinTimes[0])
        csv_writer.writerow(['n=2']+taylorSinTimes[1])
        csv_writer.writerow(['n=3']+taylorSinTimes[2])
        csv_writer.writerow(['n=4']+taylorSinTimes[3])
        csv_writer.writerow(['n=8']+taylorSinTimes[4])
        csv_writer.writerow(['n=16']+taylorSinTimes[5])
        csv_writer.writerow(['n=32']+taylorSinTimes[6])
        csv_writer.writerow(['n=64']+taylorSinTimes[7])
        csv_writer.writerow(['n=128']+taylorSinTimes[8])
        csv_writer.writerow(['n=256']+taylorSinTimes[9])
    
    with open ('taylor_sin_absolute_error_data.csv',mode='w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['','x=1/32','x=1/16','x=1/8','x=1/4','x=1/2','x=1','x=2','x=4'])
        csv_writer.writerow(['n=1']+taylorSinAbsoluteErrors[0])
        csv_writer.writerow(['n=2']+taylorSinAbsoluteErrors[1])
        csv_writer.writerow(['n=3']+taylorSinAbsoluteErrors[2])
        csv_writer.writerow(['n=4']+taylorSinAbsoluteErrors[3])
        csv_writer.writerow(['n=8']+taylorSinAbsoluteErrors[4])
        csv_writer.writerow(['n=16']+taylorSinAbsoluteErrors[5])
        csv_writer.writerow(['n=32']+taylorSinAbsoluteErrors[6])
        csv_writer.writerow(['n=64']+taylorSinAbsoluteErrors[7])
        csv_writer.writerow(['n=128']+taylorSinAbsoluteErrors[8])
        csv_writer.writerow(['n=256']+taylorSinAbsoluteErrors[9])
    
    with open ('taylor_sin_relative_error_data.csv',mode='w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['','x=1/32','x=1/16','x=1/8','x=1/4','x=1/2','x=1','x=2','x=4'])
        csv_writer.writerow(['n=1']+taylorSinRelativeErrors[0])
        csv_writer.writerow(['n=2']+taylorSinRelativeErrors[1])
        csv_writer.writerow(['n=3']+taylorSinRelativeErrors[2])
        csv_writer.writerow(['n=4']+taylorSinRelativeErrors[3])
        csv_writer.writerow(['n=8']+taylorSinRelativeErrors[4])
        csv_writer.writerow(['n=16']+taylorSinRelativeErrors[5])
        csv_writer.writerow(['n=32']+taylorSinRelativeErrors[6])
        csv_writer.writerow(['n=64']+taylorSinRelativeErrors[7])
        csv_writer.writerow(['n=128']+taylorSinRelativeErrors[8])
        csv_writer.writerow(['n=256']+taylorSinRelativeErrors[9])

main()