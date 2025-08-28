n = int(input("enter the number:\n"))
for i in range(1,n+1):
    for j in range(2,i+1):
        print("_",end=" ")
    for k in range(i,n+1):
        print("*",end=" ")
    print()

# Output:
# * * * * * 
# _ * * * * 
# _ _ * * * 
# _ _ _ * * 
# _ _ _ _ * 