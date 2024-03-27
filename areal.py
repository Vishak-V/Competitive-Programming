x=int(input())
s=x**(0.5)
t=s*4
if t%1==0:
    print(int(t))
    quit()
print("{0:.20f}".format(t))