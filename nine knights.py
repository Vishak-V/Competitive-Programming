l=[]
s=0
for i in range(5):
    n=list(input())
    for j in range (len(n)):
        if n[j]=='k':
            s=s+1
            l.append([i,j])
#print(l)
if s!=9:
    print("invalid")
    quit()
for i in l:
    if [i[0]+2,i[1]+1] in l:
        print("invalid")
        quit()
    if [i[0]+2,i[1]-1] in l:
        print("invalid")
        quit()

    if [i[0]-2,i[1]+1] in l:
        print("invalid")
        quit()
    if [i[0]-2,i[1]-1] in l:
        print("invalid")
        quit()
    if [i[0]+1,i[1]+2] in l:
        print("invalid")
        quit()
    if [i[0]+1,i[1]-2] in l:
        print("invalid")
        quit()
    if [i[0]-1,i[1]+2] in l:
        print("invalid")
        quit()
    if [i[0]-1,i[1]-2] in l:
        print("invalid")
        quit()

                    
            
    
print("valid")
