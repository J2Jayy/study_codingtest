N,M,B = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(N)]
print(N,M,B,map)

countlist = [0 for _ in range(N*M)]

for i in range(N):
    for j in range(M):
        countlist[map[i][j]] += 1
max = countlist.index(max(countlist))
print(max)
