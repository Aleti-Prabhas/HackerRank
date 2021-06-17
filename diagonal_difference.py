n=int(input())

m=[]
for i in range (0,n):
    l=[]
    l=list(map(int,input().strip().split()))[:n]
    m.append(l)

su=0
for i in range (0,n):
    for j in range (0,n):
        if(i is j):
            su=su+m[i][j]
suu=0
for i in range (0,n):
    for j in range(n-1,-1,-1):
        if(i+j==n-1):
            suu=suu+m[i][j]

add=0
if(su>suu):
    add=su-suu
else:
    add=suu-su
print(add)
