import math
import time
import csv
from decimal import Decimal

def taylorCos(x,n):
    start_time = time.time()
    s = 0
    for k in range(0,n+1):
        s += (Decimal(((-1)**k))*(Decimal((x**(2*k)))/(Decimal(math.factorial(2*k)))))
    end_time = time.time()
    total_time = end_time - start_time
    s = float(s)
    return s, total_time

def main():
    X=[0.03125,0.0625,0.125,0.25,0.5,1,2,4]
    N=[1,2,3,4,8,16,32,64,128,256]
    taylorCoss=[[0.0 for i in range(len(X))] for j in range(len(N))]
    taylorCosTimes=[[0.0 for i in range(len(X))] for j in range(len(N))]
    cosExactValues=[math.cos(x) for x in X]

    for i in range(len(N)):
        for j in range(len(X)):
            taylorcos, taylorcostime = taylorCos(X[j],N[i])
            taylorCoss[i][j] = taylorcos
            taylorCosTimes[i][j] = taylorcostime
    
    for i in range(len(X)):
        for j in range(len(N)):
            if (X[i] <= 0.0625):
                print(f'x={X[i]}\tn={N[j]}\t     cos(x)={taylorCoss[j][i]}\t\ttime={taylorCosTimes[j][i]}')
            else:
                print(f'x={X[i]}\t\tn={N[j]}\t     cos(x)={taylorCoss[j][i]}\t\ttime={taylorCosTimes[j][i]}')
        if (X[i] <= 0.0625):
            print(f'x={X[i]}\t\tExact Value={cosExactValues[i]}\n')
        else:
            print(f'x={X[i]}\t\t\tExact Value={cosExactValues[i]}\n')

    taylorCosAbsoluteErrors=[[0.0 for i in range(len(X))] for j in range(len(N))]
    taylorCosRelativeErrors=[[0.0 for i in range(len(X))] for j in range(len(N))]
    for i in range(len(N)):
        for j in range(len(X)):
            taylorCosAbsoluteErrors[i][j]=((cosExactValues[j])-(taylorCoss[i][j]))
            taylorCosRelativeErrors[i][j]=abs(((taylorCosAbsoluteErrors[i][j])/(taylorCoss[i][j]))*100)

    with open ('taylor_cos_data.csv',mode='w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['','x=1/32','x=1/16','x=1/8','x=1/4','x=1/2','x=1','x=2','x=4'])
        csv_writer.writerow(['n=1']+taylorCoss[0])
        csv_writer.writerow(['n=2']+taylorCoss[1])
        csv_writer.writerow(['n=3']+taylorCoss[2])
        csv_writer.writerow(['n=4']+taylorCoss[3])
        csv_writer.writerow(['n=8']+taylorCoss[4])
        csv_writer.writerow(['n=16']+taylorCoss[5])
        csv_writer.writerow(['n=32']+taylorCoss[6])
        csv_writer.writerow(['n=64']+taylorCoss[7])
        csv_writer.writerow(['n=128']+taylorCoss[8])
        csv_writer.writerow(['n=256']+taylorCoss[9])
        csv_writer.writerow(['Exact Value']+cosExactValues)
    
    with open ('taylor_cos_time_data.csv',mode='w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['','x=1/32','x=1/16','x=1/8','x=1/4','x=1/2','x=1','x=2','x=4'])
        csv_writer.writerow(['n=1']+taylorCosTimes[0])
        csv_writer.writerow(['n=2']+taylorCosTimes[1])
        csv_writer.writerow(['n=3']+taylorCosTimes[2])
        csv_writer.writerow(['n=4']+taylorCosTimes[3])
        csv_writer.writerow(['n=8']+taylorCosTimes[4])
        csv_writer.writerow(['n=16']+taylorCosTimes[5])
        csv_writer.writerow(['n=32']+taylorCosTimes[6])
        csv_writer.writerow(['n=64']+taylorCosTimes[7])
        csv_writer.writerow(['n=128']+taylorCosTimes[8])
        csv_writer.writerow(['n=256']+taylorCosTimes[9])
    
    with open ('taylor_cos_absolute_error_data.csv',mode='w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['','x=1/32','x=1/16','x=1/8','x=1/4','x=1/2','x=1','x=2','x=4'])
        csv_writer.writerow(['n=1']+taylorCosAbsoluteErrors[0])
        csv_writer.writerow(['n=2']+taylorCosAbsoluteErrors[1])
        csv_writer.writerow(['n=3']+taylorCosAbsoluteErrors[2])
        csv_writer.writerow(['n=4']+taylorCosAbsoluteErrors[3])
        csv_writer.writerow(['n=8']+taylorCosAbsoluteErrors[4])
        csv_writer.writerow(['n=16']+taylorCosAbsoluteErrors[5])
        csv_writer.writerow(['n=32']+taylorCosAbsoluteErrors[6])
        csv_writer.writerow(['n=64']+taylorCosAbsoluteErrors[7])
        csv_writer.writerow(['n=128']+taylorCosAbsoluteErrors[8])
        csv_writer.writerow(['n=256']+taylorCosAbsoluteErrors[9])
    
    with open ('taylor_cos_relative_error_data.csv',mode='w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['','x=1/32','x=1/16','x=1/8','x=1/4','x=1/2','x=1','x=2','x=4'])
        csv_writer.writerow(['n=1']+taylorCosRelativeErrors[0])
        csv_writer.writerow(['n=2']+taylorCosRelativeErrors[1])
        csv_writer.writerow(['n=3']+taylorCosRelativeErrors[2])
        csv_writer.writerow(['n=4']+taylorCosRelativeErrors[3])
        csv_writer.writerow(['n=8']+taylorCosRelativeErrors[4])
        csv_writer.writerow(['n=16']+taylorCosRelativeErrors[5])
        csv_writer.writerow(['n=32']+taylorCosRelativeErrors[6])
        csv_writer.writerow(['n=64']+taylorCosRelativeErrors[7])
        csv_writer.writerow(['n=128']+taylorCosRelativeErrors[8])
        csv_writer.writerow(['n=256']+taylorCosRelativeErrors[9])
        
main()