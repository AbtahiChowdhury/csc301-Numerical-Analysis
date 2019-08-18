import math
import time
import csv
from decimal import Decimal

def taylorExp(x,n):
    start_time = time.time()
    s = 0
    for k in range(0,n+1):
        s += (Decimal(x**k)/Decimal(math.factorial(k)))
    end_time = time.time()
    total_time = end_time - start_time
    s = float(s)
    return s, total_time

def main():
    X=[0.03125,0.0625,0.125,0.25,0.5,1,2,4]
    N=[1,2,3,4,8,16,32,64,128,256]
    taylorExps=[[0.0 for i in range(len(X))] for j in range(len(N))]
    taylorExpTimes=[[0.0 for i in range(len(X))] for j in range(len(N))]
    expExactValues=[math.exp(x) for x in X]

    for i in range(len(N)):
        for j in range(len(X)):
            taylorexp, taylorexptime = taylorExp(X[j],N[i])
            taylorExps[i][j] = taylorexp
            taylorExpTimes[i][j] = taylorexptime
    
    for i in range(len(X)):
        for j in range(len(N)):
            if (X[i] <= 0.0625):
                print(f'x={X[i]}\tn={N[j]}\t     exp(x)={taylorExps[j][i]}\t\ttime={taylorExpTimes[j][i]}')
            else:
                print(f'x={X[i]}\t\tn={N[j]}\t     exp(x)={taylorExps[j][i]}\t\ttime={taylorExpTimes[j][i]}')
        if (X[i] <= 0.0625):
            print(f'x={X[i]}\t\tExact Value={expExactValues[i]}\n')
        else:
            print(f'x={X[i]}\t\t\tExact Value={expExactValues[i]}\n')

    taylorExpAbsoluteErrors=[[0.0 for i in range(len(X))] for j in range(len(N))]
    taylorExpRelativeErrors=[[0.0 for i in range(len(X))] for j in range(len(N))]
    for i in range(len(N)):
        for j in range(len(X)):
            taylorExpAbsoluteErrors[i][j]=((expExactValues[j])-(taylorExps[i][j]))
            taylorExpRelativeErrors[i][j]=abs(((taylorExpAbsoluteErrors[i][j])/(taylorExps[i][j]))*100)

    with open ('taylor_exp_data.csv',mode='w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['','x=1/32','x=1/16','x=1/8','x=1/4','x=1/2','x=1','x=2','x=4'])
        csv_writer.writerow(['n=1']+taylorExps[0])
        csv_writer.writerow(['n=2']+taylorExps[1])
        csv_writer.writerow(['n=3']+taylorExps[2])
        csv_writer.writerow(['n=4']+taylorExps[3])
        csv_writer.writerow(['n=8']+taylorExps[4])
        csv_writer.writerow(['n=16']+taylorExps[5])
        csv_writer.writerow(['n=32']+taylorExps[6])
        csv_writer.writerow(['n=64']+taylorExps[7])
        csv_writer.writerow(['n=128']+taylorExps[8])
        csv_writer.writerow(['n=256']+taylorExps[9])
        csv_writer.writerow(['Exact Value']+expExactValues)
    
    with open ('taylor_exp_time_data.csv',mode='w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['','x=1/32','x=1/16','x=1/8','x=1/4','x=1/2','x=1','x=2','x=4'])
        csv_writer.writerow(['n=1']+taylorExpTimes[0])
        csv_writer.writerow(['n=2']+taylorExpTimes[1])
        csv_writer.writerow(['n=3']+taylorExpTimes[2])
        csv_writer.writerow(['n=4']+taylorExpTimes[3])
        csv_writer.writerow(['n=8']+taylorExpTimes[4])
        csv_writer.writerow(['n=16']+taylorExpTimes[5])
        csv_writer.writerow(['n=32']+taylorExpTimes[6])
        csv_writer.writerow(['n=64']+taylorExpTimes[7])
        csv_writer.writerow(['n=128']+taylorExpTimes[8])
        csv_writer.writerow(['n=256']+taylorExpTimes[9])
    
    with open ('taylor_exp_absolute_error_data.csv',mode='w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['','x=1/32','x=1/16','x=1/8','x=1/4','x=1/2','x=1','x=2','x=4'])
        csv_writer.writerow(['n=1']+taylorExpAbsoluteErrors[0])
        csv_writer.writerow(['n=2']+taylorExpAbsoluteErrors[1])
        csv_writer.writerow(['n=3']+taylorExpAbsoluteErrors[2])
        csv_writer.writerow(['n=4']+taylorExpAbsoluteErrors[3])
        csv_writer.writerow(['n=8']+taylorExpAbsoluteErrors[4])
        csv_writer.writerow(['n=16']+taylorExpAbsoluteErrors[5])
        csv_writer.writerow(['n=32']+taylorExpAbsoluteErrors[6])
        csv_writer.writerow(['n=64']+taylorExpAbsoluteErrors[7])
        csv_writer.writerow(['n=128']+taylorExpAbsoluteErrors[8])
        csv_writer.writerow(['n=256']+taylorExpAbsoluteErrors[9])
    
    with open ('taylor_exp_relative_error_data.csv',mode='w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['','x=1/32','x=1/16','x=1/8','x=1/4','x=1/2','x=1','x=2','x=4'])
        csv_writer.writerow(['n=1']+taylorExpRelativeErrors[0])
        csv_writer.writerow(['n=2']+taylorExpRelativeErrors[1])
        csv_writer.writerow(['n=3']+taylorExpRelativeErrors[2])
        csv_writer.writerow(['n=4']+taylorExpRelativeErrors[3])
        csv_writer.writerow(['n=8']+taylorExpRelativeErrors[4])
        csv_writer.writerow(['n=16']+taylorExpRelativeErrors[5])
        csv_writer.writerow(['n=32']+taylorExpRelativeErrors[6])
        csv_writer.writerow(['n=64']+taylorExpRelativeErrors[7])
        csv_writer.writerow(['n=128']+taylorExpRelativeErrors[8])
        csv_writer.writerow(['n=256']+taylorExpRelativeErrors[9])
        
main()