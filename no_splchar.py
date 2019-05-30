s=input()
c=0
l=['.','!','@','#','$','%','^','&','*','_']
for i in s:
    for j in l:
        if(i==j):
            c+=1
print(c)
            
