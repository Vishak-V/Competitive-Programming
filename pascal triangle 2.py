import math
n=int(input())
x=0
print(1)
print(1,1)
for i in range(2,n):
    for j in range(0,i+1):
        print(int(math.factorial(i)/(math.factorial(i-j)*math.factorial(j))),end = " ")
    
    print()
