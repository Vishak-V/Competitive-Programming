l=list(map(int,input().split(" ")))
n=l[0]
m=l[1]
matrix=[]
c=0
for i in range(n):
    s=input()
    matrix.append(s)
for j in range(m):
    blank=1
    for i in range(n):
        if matrix[i][j]=='$':
            blank=0
            break
    if blank==1:
        c=c+1
print(c+1)

        

