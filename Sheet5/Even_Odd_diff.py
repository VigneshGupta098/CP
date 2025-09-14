A = [1,2,3,4]
even = 0
odd = 0
for i in A:
    if i%2==0:
        even = even+1
    if i%2!=0:
        odd = odd+1
difference = even-odd
print(difference)

# Output:
# 0