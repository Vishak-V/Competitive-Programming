l=list(map(int,input().split(" ")))
w=0
s=l[1]
for i in range(l[0]):
    q=input()
    if len(q)==2:
        w=w+1
    w=w+int(q[0])
t=w/s
#print(t)
if t%1==0:
    print(int(t)-1)
else:
    print(int(t))
