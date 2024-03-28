"""
어떤 수 N이 1이 될때까지 두 과정중 하나를 반복 수행하려고 한다.
단, 두번째 연산은 N이 K 로 나누어 떨어질때만 선택할수 있다
1. N-=1
2. N/K
1번 혹은 2번 과정을 수행해야하는 최소 회숫는?
"""
count = 0
N,K = map(int,input().split())
while(N != 1):
    if N%K == 0:
        N //= K
        count += 1
    else :
        N -= 1
        count += 1
print(count)