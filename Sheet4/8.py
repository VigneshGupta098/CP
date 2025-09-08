n = int(input())
for i in range(1,n+1):
    for j in range(1,n-2):
        if i==3 and j==2:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()

# Output:
# 5
# * * 
# * * 
# *   
# * * 
# * * 