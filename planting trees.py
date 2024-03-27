n=int(input())
l=list(map(int,input().split(" ")))

l.sort()
q=[]
for i in range(len(l)):
    q.append(l[i]-i)
print(max(q)+len(l)+1)
