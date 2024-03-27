n=int(input())
for i in range(n):
    x=list(input())
    l=x
    q=l
    c=0
    for i in l:
        if i!='0':
            c+=1
    print(c)      
    for i in range(len(x)):         
          if x[i]!='0':          
              print(int(x[i])*10**(len(x)-i-1),end=" ")
        
        
    print()
