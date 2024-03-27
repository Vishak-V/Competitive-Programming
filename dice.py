def exp(a,b):
    
    return (a+b)/2

x=input()
x=x.split(" ")
for i in range(0,len(x)):
    x[i]=int(x[i])

y=input()
y=y.split(" ")
for i in range(0,len(y)):
    y[i]=int(y[i])

s1=exp(x[0],x[1])+exp(x[2],x[3])
s2=exp(y[0],y[1])+exp(y[2],y[3])

if(s1==s2):
    print("Tie")
elif(s1>s2):
    print("Gunnar")
else:
    print("Emma")
    
