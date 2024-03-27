

def func(s):
    
    l=[]
    for i in range(len(s)):
        l.append(s[i:len(s)/2])
    for i in range(len(s)):
        if(i==len(s)-1):
            return s
        else:
            x=s[i:len(s)/2]
            if(l.find(x)!=-1):
                temp=s[i]
                s[i]=s[i+1]
                s[i+1]=temp
                return func(s)
            
s=input()
print(func(s))
