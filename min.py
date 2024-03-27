x=input()
x=x.split(" ")
for i in range(len(x)):
    x[i]=int(x[i])
l=[]
for i in range(len(x)):
    for j in range(len(x)):
        if(i!=j):
            l.append(x[i]*x[j])
for i in range(len(x)):
    for j in range(len(x)):
        if(i!=j and x[i]%x[j]==0):
            l.append(x[i]/x[j])
for i in range(len(x)):
    for j in range(len(x)):
        if(i!=j):
            l.append(x[i]+x[j])
for i in range(len(x)):
    for j in range(len(x)):
        if(i!=j):
            l.append(x[i]-x[j])
#print(l)        
m=10000000000000000000           
for i in x:
    for j in l:
        c=i-j
        if(c<m and c>=0 ):
            m=c
        if(j!=0 and i%j==0):
            c=i/j
            if(c<m and c>=0):
                m=c
        c=i+j
        if(c<m and c>=0 ):
            m=c
        c=i*j
        if(c<m and c>=0 ):
            m=c
        if(i!=0 and j%i==0):
            c=j/i
            if(c<m and c>=0):
                m=c
        c=j-i
        if(c<m and c>=0 ):
            m=c 
            
print(m)                
                        

    
