n=int(input())
lst=[]
c=0
d=0
p=0
a=input().split(" ")
for i in a:
    if(int(i)>0):
        c+=1
    elif(int(i)<0):
        d+=1
    else:
        p+=1
k=c/n
l=d/n
m=p/n
print("{:.6f}".format(k))
print("{:.6f}".format(l))
print("{:.6f}".format(m))