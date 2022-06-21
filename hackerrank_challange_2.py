s=input().split(" ")
lst=[]
for i in s:
#     l=int(i)
    lst.append(int(i))
print(lst)
h=min(lst)

k=max(lst)
su=0
d=0
# lst3=lst
lst2=lst.copy()
lst.remove(k)
for i in lst:
    print(lst)
    d=d+i

lst2.remove(h)
for i in lst2:
    su=su + i
print(d ,su)