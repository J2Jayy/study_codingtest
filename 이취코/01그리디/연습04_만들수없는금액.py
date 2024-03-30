N = int(input())
coinlist = list(map(int,input().split()))
coinlist.sort()
target = 1

for i in coinlist:
    if target< i:
        print(target)
        break
    else:
        target += i