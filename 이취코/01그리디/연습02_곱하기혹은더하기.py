S = list(map(int,input()))
result = S[0]
for i in range(1,len(S)):
    if S[i] !=  0 and result != 0:
        result *= S[i]
    else:
        result += S[i]
    
print(result)

    