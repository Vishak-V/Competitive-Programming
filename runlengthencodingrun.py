l=list(input().split(" "))
#print(l)

if l[0]=='E':
    s=l[1]
    i=0
    ch=''
    c=1
    if len(s)==1:
        print(str(s),end="")
        print(1)
        quit()
    while i<len(s):
        if i+1<len(s) and s[i]==s[i+1]: 
            c=c+1
            i=i+1
        if i+1==len(s) or s[i]!=s[i+1]:
            ch=s[i]
            print(ch,end="")
            print(c,end="")
            i=i+1
            c=1

if l[0]=='D':
    s=l[1]
    i=0
    while i<len(s):
        print(s[i]*int(s[i+1]),end="")
        i=i+2


