nu=int(input())
for i in range(2,nu):
    if(nu%i==0):
        print("No")
        break
else:
    print("yes")
