n=int(input())
l=list(map(int,input().split(" ")))
l.sort()
#print(l)
i=0
if len(l)==1:
    print("N")
    quit()
k=l[0]
c=0
br=0
while i<len(l)-1:
    if l[i]==k:
        c=c+1
        del l[i]
        #print(l)
    else:
        r=c/2
        if(r==int(r)):
            l=[k+1]*int(r)+l
                
        else:
            if(k>l[i]):
                l=[k]+[k+1]*int(r)+l
            br=br+1
            if(br==2):
                print("N")
                quit()
        k=k+1
        c=0
    
        i=i+1
print(l)    
if(len(l)<3):
    print("Y")
else:
    print("N")
