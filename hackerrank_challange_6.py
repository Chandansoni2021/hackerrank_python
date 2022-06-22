
s=int(input())
d=[]
sum1=0
sum2=0
for i in range(0,s):
    a=(input()).split(" ")
    d.append(a)
for i in range(0,s):
    sum1=sum1+int(d[i][i])
for i in range(0,s):
    for j in range(0,s):
        if(i+j==2):
             sum2=sum2+int(d[i][j])
print(sum1)
print(sum2)
o=abs(sum1-sum2)
print(o)