n=int(input())
l=list(map(int,input().strip().split()))[:n]
plus=0
minus=0
zeroes=0
for i in range(0,n):
    if(l[i]>0):
        plus=plus+1
    elif(l[i]<0):
        minus=minus+1
    elif(l[i]==0):
        zeroes=zeroes+1
print(plus/n)
print(minus/n)
print(zeroes/n)