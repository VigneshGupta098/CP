n = int(input("enter the number:\n"))
for i in range(1,n+1):
    for j in range(i,n+3):
        if j==i or j==n+2:
            print("*",end=" ")
        else:
            print("_",end=" ")
    print()

# Output:
# * _ _ _ _ _ * 
# * _ _ _ _ * 
# * _ _ _ * 
# * _ _ * 
# * _ *