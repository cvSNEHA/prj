#1
print('hi...')

#2
def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
    print()

fib(12)

#3
n=int(input('number='))
a,b=0,1
while a<n:
    print(a,end=' ')
    a,b=b,a+b
print()