l=list(map(int,input().split(" ")))
d={}
n=l[0]
p=l[1]
m=l[2]
br=0
for i in range(n):
    x=input()
    d[x]=0
if m==0:
    print("No winner!")
for i in range(m):
    s=list(input().split(" "))
    #print(s)
    name=s[0]
    points=int(s[1])
    d[name]=d[name]+points
    if d[name]>=p:
        print(name+ " wins!")
        d[name]=-999999999999
        br=br+1
    if br==n:
        quit()
if br==0:
    print("No winner!")