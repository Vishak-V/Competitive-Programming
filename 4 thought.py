l=[]
s=0
q=['/','*','+','-']
for i in range(4):
    for j in range(4):
        for k in range(4):
            l.append(q[i]+q[j]+q[k])
            
m=set(l)
t=[]
ss=[]
st="4"
s=4
#print(m)
a=[]
r="4"
#print(l)
for i in l:
    r="4"
    for j in i:
        r=r+j
        r=r+"4"
    a.append(r)
#print(a)
b=a
#print(a)
for r in a:
    st="4"
    s=0
    o=a.index(r)
    j=0
    while j in range(len(r)):
        if r[j]=='*':
            s=s+int(r[j-1])*int(r[j+1])
            r=r[:j-1]+str(int(r[j-1])*int(r[j+1]))+r[j+2:]
            j=j-1
            st=st+" * 4 "
        if r[j]=='/':
            s=s+int(r[j-1])/int(r[j+1])
            r=r[:j-1]+str(int(int(r[j-1])/int(r[j+1])))+r[j+2:]
            j=j-1
            st=st+" / 4 "
        j=j+1
    while j in range(len(r)):
        if r[j]=='+':
            s=s+int(r[j-1])+int(r[j+1])
            r=r[:j-1]+str(int(r[j-1])+int(r[j+1]))+r[j+2:]
            j=j-1
            st=st+" + 4 "
        if r[j]=='-':
            s=s+int(r[j-1])-int(r[j+1])
            r=r[:j-1]+str(int(r[j-1])-int(r[j+1]))+r[j+2:]
            j=j-1
            st=st+" - 4 "
        j=j+1
    print(r)
    z=float(r)
        
    if z not in ss:
        t.append([z,b[o]])
        ss.append(z)
print(t)
print(ss)
#print(t)
n=int(input())
for i in range(n):
    x=int(input())
    if x in ss:
        print(t[ss.index(x)][1])
    else:
        print("no solution")
