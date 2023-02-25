num=int(input())
ls=[]
for i in range (num):
    j=1
    i+=1
    while j != i+1:
        ls.append(i*j)
        j=j+1
    print(ls, end=" ")
    ls=[]