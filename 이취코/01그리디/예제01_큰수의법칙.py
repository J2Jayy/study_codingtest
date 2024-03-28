"""
첫째줄에 공백으로 구분된 N,M,K가 주어진다.
둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 1이상 10000 이하이며 공백으로 구분된다
K<= M
더하는 회수는M이며, 최대로  연속해서 더할수 있는 회수가 K 일때 배열 N 에서 더하여 만들수 있는 가장 큰 수를 구하여라.
첫쨰 줄에 큰 수의 법칙에 따라 더해진 답을 출력.
"""
answer = 0
count = 0
N,M,K = map(int,input().split())
numlist = list(map(int,input().split()))
numlist.sort(reverse=True)
count =  ((M//(K+1))*K )+ (M%(K+1))
answer += count*numlist[0]
answer += (M-count)*numlist[1]
print(answer)

