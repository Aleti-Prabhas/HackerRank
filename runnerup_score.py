n = int(input())
arr = list(map(int, input().split()[:n]))
x=max(arr)
while x in arr: 
    arr.remove(x)

print(max(arr))
