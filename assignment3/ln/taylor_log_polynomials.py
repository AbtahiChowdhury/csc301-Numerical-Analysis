import math
import time
import csv
from decimal import Decimal

def taylorLog(x,n):
    start_time = time.time()
    s = 0
    for k in range(1,n+1):
        s -= (Decimal(x**k)/Decimal(k))
    end_time = time.time()
    total_time = end_time - start_time
    s = float(s)
    return s, total_time

def main():
    X=[0.03125,0.0625,0.125,0.25,0.5]
    N=[1,2,3,4,8,16,32,64,128,256]
    taylorLogs=[[0.0 for i in range(len(X))] for j in range(len(N))]
    taylorLogTimes=[[0.0 for i in range(len(X))] for j in range(len(N))]
    logExactValues=[math.log(1-x) for x in X]

    for i in range(len(N)):
        for j in range(len(X)):
            taylorlog, taylorlogtime = taylorLog(X[j],N[i])
            taylorLogs[i][j] = taylorlog
            taylorLogTimes[i][j] = taylorlogtime
    
    for i in range(len(X)):
        for j in range(len(N)):
            if (X[i] <= 0.0625):
                print(f'x={X[i]}\tn={N[j]}\t     log(x)={taylorLogs[j][i]}\t\ttime={taylorLogTimes[j][i]}')
            else:
                print(f'x={X[i]}\t\tn={N[j]}\t     log(x)={taylorLogs[j][i]}\t\ttime={taylorLogTimes[j][i]}')
        if (X[i] <= 0.0625):
            print(f'x={X[i]}\t\tExact Value={logExactValues[i]}\n')
        else:
            print(f'x={X[i]}\t\t\tExact Value={logExactValues[i]}\n')

    taylorLogAbsoluteErrors=[[0.0 for i in range(len(X))] for j in range(len(N))]
    taylorLogRelativeErrors=[[0.0 for i in range(len(X))] for j in range(len(N))]
    for i in range(len(N)):
        for j in range(len(X)):
            taylorLogAbsoluteErrors[i][j]=((logExactValues[j])-(taylorLogs[i][j]))
            taylorLogRelativeErrors[i][j]=abs(((taylorLogAbsoluteErrors[i][j])/(taylorLogs[i][j]))*100)

    with open ('taylor_log_data.csv',mode='w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['','x=1/32','x=1/16','x=1/8','x=1/4','x=1/2'])
        csv_writer.writerow(['n=1']+taylorLogs[0])
        csv_writer.writerow(['n=2']+taylorLogs[1])
        csv_writer.writerow(['n=3']+taylorLogs[2])
        csv_writer.writerow(['n=4']+taylorLogs[3])
        csv_writer.writerow(['n=8']+taylorLogs[4])
        csv_writer.writerow(['n=16']+taylorLogs[5])
        csv_writer.writerow(['n=32']+taylorLogs[6])
        csv_writer.writerow(['n=64']+taylorLogs[7])
        csv_writer.writerow(['n=128']+taylorLogs[8])
        csv_writer.writerow(['n=256']+taylorLogs[9])
        csv_writer.writerow(['Exact Value']+logExactValues)
    
    with open ('taylor_log_time_data.csv',mode='w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['','x=1/32','x=1/16','x=1/8','x=1/4','x=1/2'])
        csv_writer.writerow(['n=1']+taylorLogTimes[0])
        csv_writer.writerow(['n=2']+taylorLogTimes[1])
        csv_writer.writerow(['n=3']+taylorLogTimes[2])
        csv_writer.writerow(['n=4']+taylorLogTimes[3])
        csv_writer.writerow(['n=8']+taylorLogTimes[4])
        csv_writer.writerow(['n=16']+taylorLogTimes[5])
        csv_writer.writerow(['n=32']+taylorLogTimes[6])
        csv_writer.writerow(['n=64']+taylorLogTimes[7])
        csv_writer.writerow(['n=128']+taylorLogTimes[8])
        csv_writer.writerow(['n=256']+taylorLogTimes[9])
    
    with open ('taylor_log_absolute_error_data.csv',mode='w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['','x=1/32','x=1/16','x=1/8','x=1/4','x=1/2'])
        csv_writer.writerow(['n=1']+taylorLogAbsoluteErrors[0])
        csv_writer.writerow(['n=2']+taylorLogAbsoluteErrors[1])
        csv_writer.writerow(['n=3']+taylorLogAbsoluteErrors[2])
        csv_writer.writerow(['n=4']+taylorLogAbsoluteErrors[3])
        csv_writer.writerow(['n=8']+taylorLogAbsoluteErrors[4])
        csv_writer.writerow(['n=16']+taylorLogAbsoluteErrors[5])
        csv_writer.writerow(['n=32']+taylorLogAbsoluteErrors[6])
        csv_writer.writerow(['n=64']+taylorLogAbsoluteErrors[7])
        csv_writer.writerow(['n=128']+taylorLogAbsoluteErrors[8])
        csv_writer.writerow(['n=256']+taylorLogAbsoluteErrors[9])
    
    with open ('taylor_log_relative_error_data.csv',mode='w') as csv_file:
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(['','x=1/32','x=1/16','x=1/8','x=1/4','x=1/2'])
        csv_writer.writerow(['n=1']+taylorLogRelativeErrors[0])
        csv_writer.writerow(['n=2']+taylorLogRelativeErrors[1])
        csv_writer.writerow(['n=3']+taylorLogRelativeErrors[2])
        csv_writer.writerow(['n=4']+taylorLogRelativeErrors[3])
        csv_writer.writerow(['n=8']+taylorLogRelativeErrors[4])
        csv_writer.writerow(['n=16']+taylorLogRelativeErrors[5])
        csv_writer.writerow(['n=32']+taylorLogRelativeErrors[6])
        csv_writer.writerow(['n=64']+taylorLogRelativeErrors[7])
        csv_writer.writerow(['n=128']+taylorLogRelativeErrors[8])
        csv_writer.writerow(['n=256']+taylorLogRelativeErrors[9])
        
main()