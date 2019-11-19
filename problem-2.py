n = int(input())
for i in range(1,n+1):
    k = i
    for j in range(1,2*(i)):
        if(j<=i):
            print(j,end="")
        else:
            k = k - 1
            print(k,end="")
    print()

        
