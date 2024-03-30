N = input()
count = 0
prev = " "
for i in N:
    if i != prev:
        count +=1
        prev = i
print(count//2)