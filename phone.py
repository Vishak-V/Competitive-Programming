n=int(input())
a=int(n/10**7)
b=int((n-a*(10**7))/10**4)
c=n-a*(10**7)-b*(10**4)
print(a,'-',b,'-',c,sep="")
