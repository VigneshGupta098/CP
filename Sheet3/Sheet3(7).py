n = int(input("enter the number:\n"))
for i in range(1,n+1):
    for j in range(i,n):
        print("_",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()

# Output:
# _ _ _ _ * 
# _ _ _ * * 
# _ _ * * * 
# _ * * * * 
# * * * * * 


