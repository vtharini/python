def fact(nu):
    if(nu==1 or nu==0):
        return 1
    else:
        return nu*fact(nu-1)
nu=int(input())
print(fact(nu))
    
