n=int(input())
l=list(map(int,input().split(' ')))
l.sort(reverse=True)
s=0
for i in range(len(l)):
    
    if((i+1)%3==0):
        s=s+l[i]
        #print(l[i])
print(s)
