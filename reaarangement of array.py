import array
ch=0
n = 20#int(input('enter the range of the array : '))

a=array.array('i',[19,7,0,3,18,15,12,6,1,8,11,10,9,5,13,16,2,14,17,4])
b=array.array('i',[])
print ("the initial array is:")
for k in range(0,n):
    print(a[k], end=' ')
print("\r")
print("the final array after rearranging is:")
for i in range(0,n):
    for j in range(0,n):
        if i==a[j]:
            b.append(i)
            ch=1
            break
        else:
            ch=0
    if(ch==0):
        b.append(-1)

for k in range(0,n):
    print(b[k], end=' ')