n=int(input())
lst=[]
# c=''
for i in range(0,n):
    s=input()
    lst.append(s)    
for i in lst: 
    h=str(bin(int(i)))
    h=h[2:].zfill(32)
    for i in h:
        c=""
        if i =='1':
            c=c+'0'
        else:
            c=c+'1'
    print(int(c,base=2))
# c=""

