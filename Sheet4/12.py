n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,n):
    for j in range(i,n):
        print("*",end = " ")
    print()

# Output:
# 5
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 