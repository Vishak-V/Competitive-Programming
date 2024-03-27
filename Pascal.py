n=int(input())
if n==1:
    print(0)
    quit()
d=1
for i in range(2, int(n/2)):
    #3
    if n % i == 0:
        #4
        d = i
print(n-d)      
