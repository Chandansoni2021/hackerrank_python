s=input()
j=s
s=s.replace('AM','')
s=s.replace('PM','')
g=""
for i in range(0,2):
    g=g+(s[i])
if int(g)==12:
    s=s.replace(g,"00")
else:
    h=12+int(g)
    s=s.replace(g,str(h))
print(j)
