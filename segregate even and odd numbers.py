import array

n = 8#int(input('enter the range of the array : '))

a=array.array('i',[1,3,2,4,7,6,9,10])
print ("the initial array is:")
for k in range(0,n):
    print(a[k], end=' ')
print("\r")

for i in range(0,n):
    for j in range(n):
        if (a[j]%2!=0):
            b=a[j]
            a.pop(j)
            a.append(b)

print("the final array after moving all zeroes at end is:")

for k in range(0,n):
    print(a[k], end=' ')