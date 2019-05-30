u,v=map(int,input().split())
for nu in range(u,v):
    temp=nu
    dig=nu
    c=0
    sum=0
    while(dig!=0):
        dig=dig//10
        c+=1
    while(temp!=0):
        d=temp%10
        sum=sum+(d**c)
        temp//=10
    if(sum==nu):
        print(nu,end=" ")
