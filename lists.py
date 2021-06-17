n=int(input())
list=[]
def list_operation(operation):
    if(operation[0]=='i'):
        a,b,c=operation.split(" ")
        list.insert(int(b),int(c))
    elif(operation[0:3]=='rem'):
        a,b=operation.split(" ")
        list.remove(int(b))
    elif(operation[0]=='a'):
        a,b=operation.split(" ")
        list.append(int(b))   
    elif(operation=="pop"):
        list.pop(len(list)-1)     
    elif(operation=="print"):
        print(list)
    elif(operation=="sort"):
        list.sort()
    elif(operation=="reverse"):
        list.reverse()
    else:
        print("invalid input")
          

for i in range(0,n):
    operation=input()
    list_operation(operation)
