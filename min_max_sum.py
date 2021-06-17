n=5
l=list(map(int,input().strip().split()))[:n]
x=l[4]+l[1]+l[2]+l[3]
y=l[0]+l[4]+l[2]+l[3]
z=l[0]+l[1]+l[4]+l[3]
m=l[0]+l[1]+l[2]+l[4]
n=l[0]+l[1]+l[2]+l[3]
print(min(x,y,z,m,n),end=" ")
print(max(x,y,z,m,n))
        
