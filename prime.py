nu=int(input())
for i in range(2,nu):
    if(nu%i==0):
        print("no")
        break
else:
    print("yes")
