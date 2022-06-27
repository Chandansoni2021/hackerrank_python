n=int(input())
lst=list(map(int, input().split()))
j=[]
d=0
lst.sort()
for i in lst:
    j.append(i)
    if i not in j:
        c=lst.count(i)
        print(c,end=" ")