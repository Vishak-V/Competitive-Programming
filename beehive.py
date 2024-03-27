mat=[]
sour=0
sweet=0
while True:
    f=input()
    m=f.split()
    if m==['0.0','0']:
        break
    a='.'
    if a not in list(m[1]):
        d=float(m[0])
        n=int(m[1])
        for i in range(0,int(n)):
            l=input()
            g=l.split()
            x=float(g[0])
            y=float(g[1])
            mat.append([x,y])
        
                                    
        for i in mat:
            s=0
            dist=0
            k=[]
            for j in mat:
                c=i[0]
                v=i[1]
                dist=(((c-j[0])**2)+((v-j[1])**2))**(1/2)
                if dist!=0:
                    k.append(dist)
                
                
                   
            if d >= min(k):
                s=1
                    
            
        if s==1:
                sour=sour+1
                
    print(sour,"sour",n-sour,"sweet")                
        
    
