s=input()
u=0
d=0
w=0
try:
    for i in range(s.index('U'),len(s)-1):
        if s[i]!='U':
            u=u+2
    if s[len(s)-1]=='D':
        u=u+1
    if s[0]=='D':
        u=u+1
    for i in range(s.index('D'),len(s)-1):
        if s[i]!='D':
            d=d+2
    if s[len(s)-1]=='U':
        d=d+1
    if s[0]=='U':
        d=d+1
    for i in range(1,len(s)):
        if s[i-1]!=s[i]:
            w=w+1
    print(u)
    print(d)
    print(w)

