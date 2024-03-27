l=list(input())
for i in range(len(l)):
    l[i]=int(l[i])
sum1=l[0]+l[1]+l[2]
sum2=l[3]+l[4]+l[5]

if sum1==sum2:
    print(0)
if(sum1<sum2):
    t=sum1
    sum1=sum2
    sum2=t
    l=l[::-1]
    
if(sum1>sum2):
    dif=sum1-sum2
    l1=[l[0],l[1],l[2]]
    l2=[l[3],l[4],l[5]]
    c=0;
    wen=0
    if(abs(dif-sum1)<abs(dif-sum2)):
       wen=2
    else:
        wen=1
    if wen==1:    
        while(dif>0):
            c=c+1
            if(max(l1)-dif>0):
                print(c)
                dif=0
            else:
                dif=dif-max(l1)
    if wen==2:
        while(dif>0):
            c=c+1
            if(dif-9+min(l2)<0):
                print(c)
                dif=0
            else:
                dif=dif-9+min(l2)
            

    
