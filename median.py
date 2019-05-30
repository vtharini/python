n=int(input())
l=list(map(int,input().split()))
m=len(l)//2
l.sort()
print(l[m])
