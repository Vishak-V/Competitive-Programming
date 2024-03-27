c=0
br=1

#print(x)
for i in range(5):
    x=input()
    c=c+1
    if "FBI" in x:
        print(c,end=" ")
        br=0
    

    
    
if(br==1):
    print("HE GOT AWAY!")
        
