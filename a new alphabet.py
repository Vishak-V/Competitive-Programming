s=list(input())
#print(s[0])
for i in s:
    if(i.isalpha()):
        i=i.lower()
#print(s[0])
#for i in s:
    #print(i)
#if(s[0].isalpha()):
    #s[0]=s[0].lower()    
for i in s:
    if(not(i.isalpha())):
        print(i,end="")
        continue;
    #print(i,end="")    
    if(i=='a' or i=='A'):
        print("@",end="")
    if(i=='b' or i=='B'):
        print("8",end="")
    if(i=='c' or i=='C'):
        print("(",end="")
    if(i=='d' or i=='D'):
        print("|)",end="")
    if(i=='e' or i=='E'):
        print("3",end="")
    if(i=='f' or i=='F'):
        print("#",end="")
    if(i=='g' or i=='G'):
        print("6",end="")
    if(i=='h' or i=='H'):
        print("[-]",end="")
    if(i=='i' or i=='I'):
        print("|",end="")
    if(i=='j' or i=='J'):
        print("_|",end="")
    if(i=='k' or i=='K'):
        print("|<",end="")
    if(i=='l' or i=='L'):
        print("1",end="")
    if(i=='m' or i=='M'):
        print("[]\/[]",end="")
    if(i=='n' or i=='N'):
        print("[]\[]",end="")
    if(i=='o' or i=='O'):
        print("0",end="")
    if(i=='p' or i=='P'):
        print("|D",end="")
    if(i=='q' or i=='Q'):
        print("(,)",end="")
    if(i=='r' or i=='R'):
        print("|Z",end="")
    if(i=='s' or i=='S'):
        print("$",end="")
    if(i=='t' or i=='T'):
        print("']['",end="")
    if(i=='u' or i=='U'):
        print("|_|",end="")
    if(i=='v' or i=='V'):
        print("\/",end="")
    if(i=='w' or i=='W'):
        print("\/\/",end="")
    if(i=='x' or i=='X'):
        print("}{",end="")
    if(i=='y' or i=='Y'):
        print("`/",end="")
    if(i=='z' or i=='Z'):
        print("2",end="")
            
        
        
