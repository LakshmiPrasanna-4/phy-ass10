# Write a program to print multiplication table using for loop.

n=int(input())
a=int(input())
for i in range(1,a+1):
    r=n*i
    print(n,'*',i,'=',r)
