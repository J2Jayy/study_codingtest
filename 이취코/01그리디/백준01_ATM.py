N = int(input())
time = list(map(int,input().split()))
time.sort()
maxtime = 0
for i in range(N):
    maxtime += sum(time[0:i+1])
    
print(maxtime)