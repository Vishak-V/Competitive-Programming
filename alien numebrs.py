n=int(input())
for i in range(n):
    y=input().split(" ")
    x=list(y[0])
    l1=list(y[1])
    l2=list(y[2])
    #print(l1)
    #print(l2)
    s=0
    print("Case #",i+1,":",sep="",end=" ")
    for j in range(len(x)):
        s=s+l1.index(x[j])*(len(l1)**(len(x)-x.index(x[j])-1))
    
       # print(s)
    l=[]
    if(s==0):
        print(l2[0],end="")
    while(s>0):
        
        l.insert(0,l2[s%len(l2)])
        s=int(s/len(l2))
        
    for i in l:
        print(i,end="")
    print()  
        
