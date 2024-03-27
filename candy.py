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
    elif c>1:
        r=c/2
        if(r==int(r)):
            l=[k+1]*int(r)+l
            if(l[int(r)]<k+1):
                temp=l[r]
                l[r]=k+1
                l[0]=temp
        else:
            l=[k]+[k+1]*int(r)+l
            if(l[int(r)+1]<k+1):
                temp=l[r]
                l[r]=k+1
                l[0]=temp
            br=br+1
            if(br==2):
                print("N")
                quit()
        if(l[i]==l[i+1]):
            continue
        else:
            i=i+1
        k=l[i]
        c=0
print(l)    
if(len(l)<3):
    print("Y")
else:
    print("N")             
