import numpy as np
import matplotlib.pyplot as plt
import math
import turtle

#Ex 1
# a)

x=0

if x < np.pi or x > -np.pi:
    y = 2*np.cos(4*x) + 1
else:
    y = np.cos(6*x) + 2

#print("a) x is ", x, "and y ", y)
#print()

# b)

xs = np.linspace(-8,8,1000)
ys = np.zeros(len(xs))

for index, x in enumerate(xs):
    if -np.pi < x < np.pi:
        ys[index] = 2 * np.cos(4 * x) + 1
    else:
        ys[index] = np.cos(6 * x) + 2


plt.title("Exercice 1")
plt.xlabel("x")
plt.ylabel("y")

plt.xlim(-8,8,2)
plt.ylim(-1, 3, 0.5)

plt.plot(xs, ys)
#plt.show()

#Ex 2
#a)

def puissance(n):
    value = 1
    for i in range(n):
        value = value * 2
    return value
#print(puissance(4))

#b)
#i) for-loop
def somme(min, max):
    xs2 = np.arange(min, max + 1)
    #xs2 = np. linspace(min, max, max-min +1)

    #print(xs2)

    value = 0
    for x2 in xs2:
        if x2%5 == 0 and x2%7 ==0:
            #print("here")
            #print(value)
            value = value + x2
    return value

#print(somme(5, 71))


#ii) while-loop
def somme2(min, max):
    value = 0
    x22 = min
    while x22 <= max:
        if x22% 5 == 0 and x22 % 7 ==0:
            value = value + x22
        x22 = x22 + 1
    return value
#print(somme2(4,109))


#c)
#i)
def fact(x):
    fact = 1
    for i in range(1,x+1):
        fact = fact * i
    return fact

#ii
def fact2(x):
    fact = 1
    while x > 1:
        fact = fact * x
        x = x-1
    return fact

#d)
def division(x,y):
    i = 0
    rest = x
    while rest >= y:
        rest = rest - y
        i = i+1
    return i,rest

#print(division(21,3))


# Ex 3 - by hand!
n = 6
i,a,b = 0,0,0

while n>1:
    i = i+n
    if n%2 ==0:
        n = n//2
        a = a+1
    else:
        n = 3*n + 1
        b = b+1

#Ex 4

#c)
#v = [1, 2, 3, 4, 0, -10, 999, 10, 9, 8, 999, -10, 0, 998, 0]

#a)
#v = [0,2,4,6,8,10]
def max_in_vector(v):
    mymax = v[0]
    for a in v:
        if a > mymax:
            mymax = a
    return mymax
#print("max_vector = ",max_in_vector(v))


#b)
#i) while
def max_in_vector2(v):
    index = 0
    mymax = v[0]
    i = 0
    while i < len(v):
        if v[i] > mymax:
            mymax = v[i]
            index = i
        i = i +1
    return mymax, index
#print("max_vector2 = ",max_in_vector2(v))


#ii) for
def max_in_vector3(v):
    mymax = v[0]
    max_index = 0
    for index, value in enumerate(v):
        if value > mymax:
            mymax = value
            max_index = index
    return mymax, max_index
#print("max_vector3 = ",max_in_vector3(v))

#d)
def maxes_in_vector(v):
    v1 = v[0]
    v2 = v[1]
    for a in v:
        if a > v1 and a > v2:
            if v1 > v2:
                v2 = a
            elif v2 > v1:
                v1 = a
        elif a > v1 and a != v2:
            v1 = a
        elif a > v2 and a != v1:
            v2 = a
    return v1, v2
#print(maxes_in_vector(v))



#Ex 5
#a)
#i) if
def is_prime(x):
    if (x <= 1):
        return False
    elif (x ==2):
        return True
    else:
        racine = int(math.sqrt(x))
        for n in range(2, racine + 1):
            if (x % n == 0):
                return False
        return True

#print(is_prime(x))


#ii) while
def is_prime2(x):
    if (x <=1):
        return False
    elif (x==2):
        return True
    else:
        n = 2
        while n <= math.sqrt(x):
            if (x % n == 0):
                return False
            n = n+1
        return True


#b)
def find_primes(L):
    primes = []
    for x in L:
        if is_prime(x):
            primes.append(x)
    return primes

#or

L = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def find_primes2(L):
    return list(filter(is_prime2, L))
#print(find_primes2(L))


# Ex 6
def pgdc(a,b):
    while b !=0:
        r = a%b
        a = b
        b = r
    return a

print(pgdc(27, 36))             # 9
print(pgdc(248, 496))           # 248
print(pgdc(3840871, 2153908))   # 1987

# Ex 7

turtle.shape("turtle")

command1 = "FllFllFllFllFllFBrrrrFrrrFFRRFFFFRRFFFFRRFFFFRRFFFFRRFF"
command2 = "rFrrFLLFLLFLLFrrFBllLLFLLFrrFllFBrrrrFllFBrrrrFllFBrrrrFllF"
command3 = "lllLLFLLFLLFLLFLLFrrFrrFrrFrrFrrFrrFrrFrrFllFrrFrrFBllllFrrF"

for char in command3:
    if char == "F":
        turtle.forward(50)
    elif char == "B":
        turtle.backward(50)
    elif char == "L":
        turtle.left(36)
    elif char == "R":
        turtle.right(36)
    elif char == "l":
        turtle.left(30)
    elif char == "r":
        turtle.right(30)

turtle.getcanvas().postscript(file="turtle.eps")
turtle.done()