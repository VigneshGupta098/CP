n = int(input())
for i in range((n*2),0,-2):
    for j in range(i-1):
        print("*",end=" ")
    print()

# Output:
# 5
# * * * * * * * * * 
# * * * * * * * 
# * * * * * 
# * * * 
# * 