import statistics

N = int(input())
a =[]
for i in range(N):
    P = int(input())
    a.append(P)
S = round(sum(a)/N,1)
print(S)
M = a[len(a)//2]
print(M)
B = statistics.mode(a)
print(B)
R = max(a) - min(a)
print(R)
    