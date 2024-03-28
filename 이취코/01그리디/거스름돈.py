'''
당신은 음식점의 계산을 도와주는 점원이다, 
카운터에는 거스름돈으로 사용할 500원,100원,50원,10원짜리 동전이 무한히 존재하고,
손님에게 거슬러 줘야할 돈이 N으로 입력될때 , 거슬러 줘야 할 동전의 최소개수는?
(단, 거슬러 줘야할 돈 N은 항상 10의 배수이다.)
'''
'''
# 내 시도
N = int(input())
Coins = 0 #동전 개수
while(1):
    if N >= 500 :
        N -= 500
        Coins += 1
    elif N>=100 :
        N-= 100
        Coins += 1
    elif  N>= 50 :
        N -= 50
        Coins += 1
    elif N >= 10:
        N -= 10
        Coins += 1
    else: 
        print(Coins)
        break
'''
#더 나은 방법
N = int(input())
count = 0
coins = [500,100,50,10]
for coin in coins:
    count += N//coin
    N %= coin
print(count)
