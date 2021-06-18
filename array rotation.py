import array

n = int(input('enter the range of the array : '))
d = int(input("by how many terms you wanna rotate the array : "))

a=array.array('i',[])
b=array.array('i',[])
for m in range(0,n):
    a.append(int(input('enter ')))
print ("the initial array is:")
for k in range(0,n):
    print(a[k], end=' ')
for l in range(d,n):
    b.append(a[l])
for j in range(0,d):
    b.append(a[j])
print("\r")
print("the final array after rotation is:")
for k in range(0,n):
    print(b[k], end=' ')
