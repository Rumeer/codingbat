# Exercise 2
# 1. Write a program, factorial.py to compute a factorial of an integer, n.
number = 1
def factorial(n):
    for i in range(1,n+1):
        global number
        number = number * i
        print(number)
# factorial(6)
# 2. Write a program, fibonacci.py to compute the Fibonacci number of an integer , n.
def fibonacci(n):
    if n < 0:
        print('wrong')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(5))
# 3. The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,
# gcd(2, 12) = 2
# gcd(6, 12) = 6
# gcd(9, 12) = 3
# gcd(17, 12) = 1
# Write a program, greatest_common_divisor.py to implement this idea recursively. The function gcd() takes in two positive integers and returns one integer.
def gcd(a, b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)
# print(gcd(72,48))
# def move(n, source, bridge, destination):
#     pass # need to be modified
# move(3, 'A', 'B', 'C')
# Expected output:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
def TowerOfHanoi(n , from_rod, to_rod, aux_rod): 
    if n == 1: 
        print('Move disk 1 from rod',from_rod,'to rod',to_rod) 
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
    print('Move disk',n,'from rod',from_rod,'to rod',to_rod) 
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod) 
n = 3
TowerOfHanoi(n,'A','B','C')