u,v=map(int,input().split())
for i in range(u+1,v):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i,end=" ")
        
