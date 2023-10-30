# Write a program to print given number is a perfect number or not.

def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    if s==n:
        print('Perfect')
    else:
        print('Not Perfect')
t=int(input())
for i in range(t):
    n=int(input())
    perfect(n)
        

