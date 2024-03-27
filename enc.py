s1=input()
s2=input()
l=0
for i in range(len(s1)):
    #print(ord(s2[i]),s2[i])
    if(i%2==0):
        l=ord(s1[i])-ord(s2[i])+ord("A")
        #print(l)
        if(l<ord("A")):
            l=ord(s1[i])-ord(s2[i])+ord("A")+26
        #print(l)    
        print(chr(l),end="")
    else:
        l=ord(s1[i])+ord(s2[i])-ord("A")
        if(l>ord("Z")):
           l=ord(s1[i])+ord(s2[i])-ord("A")-26
        #print(l)   
        print(chr(l),end="")
