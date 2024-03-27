n=int(input())
for i in range(n):
    l=list(map(int,input().split(" ")))
    w=l[0]
    g=l[1]
    h=l[2]
    r=l[3]
    sm=(abs(h-g)**2+w**2)**(0.5)
    la=((w*(h/(g+h)))**2+(h-r)**2)**(0.5)+((w*(g/(g+h)))**2+(g-r)**2)**(0.5)
    test=((w/2)**2+(h-r)**2)**(0.5)+((w/2)**2+(g-r)**2)**(0.5)
    print(sm,la,test)
