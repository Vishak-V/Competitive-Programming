n=input()
q=[n.count('T'),n.count('C'),n.count('G')]
l=[0,0,0]
for i in range(len(q)):
    l[i]=q[i]**2
    
m=min(q)
print(sum(l)+7*m)
