n=input()
l=[]
v=[]
for i in n:
    if i in ('a','e','i','o','u','A','E','I','O','U'):
        l.append("")
        v.append(i)
    else:
        l.append(i)
        


i=0
while i<len(l):
    if l[i]=="":
        l[i]=v.pop()
    i=i+1    
        
print(''.join(l))    
        
        
