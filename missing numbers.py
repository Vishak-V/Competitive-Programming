x=int(input())
l=[]
for i in range(x):
    j=int(input())
    l.append(j)
i=0
t=1
br=0
while t<l[-1]:
    if t==l[i]:
        i=i+1
        t=t+1
    else:
        br=1
        print(t)
        t=t+1

if br!=1:
    print("good job")
