l=eval(input())
l.sort()
i=0
n=0
while True:
    if l[n]==2*l[i]:
        print("true")
        break
    elif l[n] > 2*l[i]:
        i=i+1
    elif l[n] < 2*l[i]:
        n=n+1
        continue
        
