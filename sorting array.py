import array

n = int(input('enter the range of the array : '))

a=array.array('i',[])

for m in range(0,n):
    a.append(int(input('enter ')))
print ("the initial array is:")
for k in range(0,n):
    print(a[k], end=' ')

print("\r")
print("the final array after sorting is:")

for i in range(n-1):
    for j in range(n-1):
        if (a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

for i in range(0,n):
    print(a[i], end=' ')