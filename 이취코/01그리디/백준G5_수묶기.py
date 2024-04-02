
N = int(input())
numlist = [int(input()) for _ in range(N)]
numlist.sort(reverse=True)
sum = 0
i = 0
while(i <= len(numlist)-1):

    if numlist[i] > 0 and numlist[i+1]> 0:
        sum += numlist[0]* numlist[1]
        i += 2
    elif  numlist[i] == 0 :
        i += 1
    elif numlist[i] < 0 and numlist[i+1] < 0:
        sum += numlist[0]* numlist[1]
    else :
        i += 1
print(sum)



