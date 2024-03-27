l=list(input())
c=0
m=0
a=ord('a')
l1=[]
#for i in l:
    #print(i)
while(a<=ord("z")):
    try:
        j=l.index(chr(a))
        l1.append(l[j])
        k=0
        l=l[j+1:]
        a=a+1
    except:
        a=a+1
    
        
print(26-len(l1))
    
