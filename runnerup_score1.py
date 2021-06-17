n = int(input())
array = list(map(int, input().split()))
ma = max(array)
i=0
while(i<n):
    if ma ==max(array):
        array.remove(max(array))
    i+=1
print(max(array))