# Ex 1

#a)
R = 3/2.0
print(R)

#b)
R = 3//2.0
print(R)

#c)
R = 3%2.0
print(R)

#d)
R = 2+3*2**3 // 2.0 +5
print(R)
#19

#e)
R = 2*2**4 <= 128/4
print(R)
#True

# i)
R = [1,2,3]
R[-1]
print(R[-1])

# j)
x = [1,2,3,4,5]
R = 3*x[:3]
print(3*x[:3])

# k)
x = list(range(10,0,-1))
R = x[-1] >= 5
print(x[-1] >= 5)

# m)
def f(x):
    print(x**2)
print(f(8))

R = 10
def f(x):
    R = x**2
    return 1
f(8)
print("n)f(8)")

# Ex 2
print("Ex 2) has been done on paper")

# Ex 3
import numpy as np
import matplotlib.pyplot as plt

n = 256
X = np.linspace(-np.pi, np.pi, n)
Y = np.sin(X)
Z = np.sin(X + np.pi / 2.0)

plt.plot(X, Y+1, color="blue")
plt.plot(X, Z-1, color="red")

plt.suptitle("n = 256",fontweight="bold")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# Ex 4
# a)


def tripleStep(x):
    if x >= -5 and x <= -1:
        return -1
    elif x> -1 and x<1:
        return 0
    elif x> 1 and x <5:
        return 1
    else:
        return " "

X = np.linspace(-5,5, 2000)
Y = [tripleStep(x) for x in X]

plt.plot(X,Y)
plt.axis([-6, 6, -2.0, 2.0])

plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

print(tripleStep(-2))
print(tripleStep(0))
print(tripleStep(4))


# Ex 5
# a)

a = 4
b = 10
c = 4
while (a < b) and (c < b):
    if (b-2*a) > 0:
        for i in range (0, a):
            c = c + 1
    elif (b-c-1) > 0:
        c = c + 1
    else:
        b = b - 2
    a = a + 1

print("a =", a)
print("b =", b)
print("c =", c)

# Ex 6

def maxima(a):
    if a[0][1] > a[0][0]:
        max1 = a[0][1]
        max2 = a[0][0]
    else:
        max1 = a[0][0]
        max2 = a[0][1]

    for row in a:
        for value in row:
            if value > max1:
                max2 = max1
                max1 = value
            elif value > max2:
                max2 = value
        return max1, max2


a = [[-1, -5, 7], [-8, 4,2], [-9,6,-3]]
print(maxima(a))


# Ex 7

# a)
# b)

import numpy as np

def ms(a):
    #a is a 2D numpy array
    rows, cols = a.shape
    s = 0
    for i in range(rows):
        for j in range(cols):
            s = s + a[i,j]
    return s

i = 10

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
value = ms(matrix)

print("Ex 7) value =", value)
print("Ex 7) i =", i)


# Ex 8

def mystery(a, b):
    if (b == 0):
        return 0
    if (b%2 == 0):
        return mystery(a+a, b//2)
    return mystery(a+a, b//2) + a


a = 25//2
print(a)