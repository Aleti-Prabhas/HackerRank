n=int(input())
l=list(map(int,input().strip().split()))[:n]
max=l[0]
for i in range(1,n):
    if(max<l[i]):
        max=l[i]
count=0
for i in range(0,n):
    if(l[i]==max):
        count=count+1

print(count)
