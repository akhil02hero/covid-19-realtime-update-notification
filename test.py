inp=input().split()
arr1s=int(inp[0])
arr2s=int(inp[1])
arr1=list()
arr2=list()

for i in range(arr1s):
    b=int(input())
    arr1.append(b)
print(arr1)

for i in range(arr2s):
    b=int(input())
    arr2.append(b)
print(arr2)

max1=max(arr1)
max2=max(arr2)
maxl=max(max1,max2)
print(maxl)