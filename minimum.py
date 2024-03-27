x=input()
x=x.split(" ")
for i in range(len(x)):
    x[i]=int(x[i])
l=[]
for i in range(len(x)):
    for j in range(len(x)):
        for k in range(len(x)):
            if(i==0 and j==1 and k==2):
                l.append((x[i]*x[j])*x[k])
                if((x[i]*x[j])%x[k]==0):
                    l.append((x[i]*x[j])/x[k])
                l.append((x[i]*x[j])-x[k])
                l.append((x[i]*x[j])+x[k])
                if(x[i]%x[j]==0):
                    l.append((x[i]/x[j])*x[k])
                    l.append((x[i]/x[j])-x[k])
                    l.append((x[i]/x[j])+x[k])
                    if((x[i]/x[j])%x[k]==0):  
                        l.append((x[i]/x[j])/x[k])
                l.append((x[i]-x[j])*x[k])
                l.append((x[i]-x[j])+x[k])
                l.append((x[i]-x[j])-x[k])
                l.append((x[i]+x[j])*x[k])
                if((x[i]+x[j])%x[k]==0):
                    l.append((x[i]+x[j])/x[k])
                if((x[i]-x[j])%x[k]==0):    
                    l.append((x[i]-x[j])/x[k])
                l.append((x[i]+x[j])+x[k])
                l.append((x[i]+x[j])-x[k])
i=0            
while i in range(len(l)):
    if(l[i]!=int(l[i]) or l[i]<0):
        del l[i]
        i=i-1
    i=i+1    
l.sort()
#print(l)
print(int(l[0]))
