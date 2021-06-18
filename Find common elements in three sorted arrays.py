import array

a=array.array('i',[5, 5, 10, 20])
b=array.array('i',[1, 5, 5])
c=array.array('i',[3, 4, 5, 5, 10])

ch=0

def min(a,b,c):
    if (len(a)<=len(b) and len(a)<=len(c)):
        n=len(a)
        return n
    elif (len(b)<=len(a) and len(b)<=len(c)):
        n=len(b)
        return n
    elif (len(c) <= len(a) and len(c) <= len(b)):
        n = len(c)
        return n
for i in range(min(a,b,c)):
    ch=0
    for j in range(len(a)):
        if (b[i]==a[j]):
            for k in range(len(c)):
                if b[i]==c[k]:
                    ch=1
                    break
    if(ch==1):
        print(b[i])