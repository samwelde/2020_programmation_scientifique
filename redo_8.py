



# Example of Bugger
######################

def f1(n):
    sum = 0
    for i in range(0,n):
        sum = sum +1
    for j in range(0,n):
        sum = sum +1
    print(i, sum, j, n)
    return sum

result = f1(4)
#print("results = ", result)
######################


# Ex 1
# a)
def count_rec(L, value):
    if len(L) == 0:
        return 0

    head = L[0]
    tail = L[1:]

    if head == value:
        return 1 + count_rec(tail, value)
    else:
        return count_rec(tail, value)

#b)
def index_rec(L, value):
     if value not in L:
        return -1
     head = L[0]
     tail = L[1:]
     if head == value:
        return 0
     else:
        return 1 + index_rec2(tail, value)

#c)
def find_max_rec(L):
     if len(L) == 1:
        return L[0]
     if L[0] > find_max_rec(L[1:]):
        return L[0]
     else:
        return find_max_rec(L[1:])

#d)

def fibonacci(n):
     if n == 0:
        return 0
     if n == 1:
        return 1
     return fibonacci(n - 1) + fibonacci(n - 2)

#e)
def binaire_rec(n):
     if n < 0:
         return "n must be positive"
     if n == 0:
        return ''
     return binaire_rec(n // 2) + str(n % 2)


# Ex 2

import random

L = [3, 6, 12, 5, 3, 7, 1, 7, 2]

def quicksort(L):
    if len(L) <= 1:
        return L
    else:
         random.shuffle(L)
         h = L[0]
         A, B = [], []
         for i in L[1:] :
            if i <= h:
                A.append(i)
            else:
                B.append(i)
         A = quicksort(A) + [h] + quicksort(B)
         return A
print("this is the L list before and...", L)
print("this is the solution after quicksort in Ex. 2)", quicksort(L))



# Ex 3
# a)

def f(a, b):
    if (b == 0):
        return 1
    elif (b % 2== 0):
        n = f(a, b//2)
        return n * n
    else:
        return a ∗f(a,b−1)

# b)
def somme_rec(L):
    if len(L) == 1:
        return L[0]
    return L[0] + somme_rec(L[1:])

# Ex 4

import turtle
import random

def brownian_motion(n):

    mu = 5
    sigma = 2

    for _ in range(n):
        random_angle = random.randint(-180, 180)
        random_dist = random.gauss(mu, sigma)

    turtle.lt(random_angle)
    turtle.fd(random_dist)

brownian_motion(1000)
turtle.getcanvas().postscript(file="brownian_motion.eps")
turtle.done
