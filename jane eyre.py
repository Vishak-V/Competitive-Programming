x=list(map(int,input().split()))
n=x[0]
m=x[1]
k=int(x[2])
#for i in r
w=[]
for i in range(n):
    l=list(input().split(" "))
    s=""
    for i in l[:-1]:
        s=s+i
        s=s+" "
    w.append((s,l[-1]))
    #print(s)
g=[]
for i in range(m):
    l=list(input().split(" "))
    s=""
    for i in l[1:-1]:
        s=s+i
        s=s+" "
    g.append((s,l[0],l[-1]))
    #print(s)
w.append(("\"Jane Eyre\"",k))
sorted_w=sorted(w,key=lambda x:x[0])
w=sorted_w
print(sorted_w)
print(g)
c=0
while i in range(len(w)):
    if(w[i][0]=='\"Jane Eyre\"'):
        print(c+k)
        quit()
    else:
        print(c)
        c=c+int(w[i][2])
        for j in g:
            if(c>=int(j[1])):
                w.append(j[0],j[2])
                g.remove(j)
                w=sorted(w,key=lambda x:x[0])
    i=i+1
                

