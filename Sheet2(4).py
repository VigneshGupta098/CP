 
# 4. Write a program to print all odd numbers from 1 to N, where you have to take N as input 
# from user. 

N = int(input("Enter a number: "))
for x in range(1, N+1):
    if (x%3==0):
        print(x,end=" ")