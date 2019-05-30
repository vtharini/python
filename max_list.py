n=int(input())
l=list(map(int,input().split()))
max=l[0]
for i in range(len(l)-1):
    if(l[i]<l[i+1]):
        max=l[i+1]
print(max)
