import array
ch=0
a=array.array('i',[1,2,3,4,5,6,7])
for i in range(0,7):
    for j in range(0,7):
        if (a[i]+a[j]==9):
            ch=1
            x=a[i]
            y=a[j]
            print("the sum of",x,"+",y,"is 9")
            break
    if(ch==1):
        break