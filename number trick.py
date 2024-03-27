x=float(input())
br=0
for i in range(1,100000000):
    s=str(i)
    q=s[1::]+s[0]
    if(x*i==int(q)):
        print(i)
        br=1
if br==0:
    print("No solution")
