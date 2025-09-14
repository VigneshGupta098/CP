A = [1,2,3,4,5]
even = []
odd = []
for i in A:
    if i%2==0:
        even.append(i)
    elif i%2!=0:
        odd.append(i)
print(*odd)
print(*even)

# Output:
# 1 3 5
# 2 4

# "*" we use thsi because it removes the list means unpack