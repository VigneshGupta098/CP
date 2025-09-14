a = list(map(int,input().split()))
max = 0
min = a[0]
for i in a:
    if i>max:
        max = i
    if i<min:
        min = i
print(max,min)

# Output:
# 5 10 15 7 20 6
# 20 5