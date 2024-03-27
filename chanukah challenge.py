n=int(input())
for i in range(n):
    l=list(map(int,input().split(" ")))
    print(i+1,int(((l[1]*(l[1]+1))/2)+l[1]))
