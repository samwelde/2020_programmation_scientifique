import numpy as np
import random


# Ex 1
# a)

n = 7

def f1(n):
    total = 0
    for i in range(0,n):
        total += 1
    for j in range(0,3*n):
        total += 1
    for k in range(0,4*n):
        total += 1
    return total

def f2(n):
    total = 0
    for _ in range(0,n):
        for _ in range (0,n):
            f1(n)
            total += 1
    return total

def f3(n):
    total = 1
    for i in range(0,2**n):
        total += 1
    return total

def f4(n):
    total = 0
    i = 1
    while i < n:
        i *=2
        total += 1
    return total

print("a) with ",n,"  f1 is =", f1(n))
print("a) with ",n," f2 is =", f2(n))
print("a) with ",n," f3 is =", f3(n))
print("a) with ",n," f4 is =", f4(n))

# b)
print("b) f1 is = n*8")
print("b) f2 is = n**2")
print("b) f3 is = 2**n + 1")
print("b) f4 is = log(n)")

print(np.log(7))
print()


# c)
print("c) f1 has the big O as O(n)")
print("c) f2 has the big O as O(n**2)* O(n) = O(n**3)")
print("c) f3 has the big O as O(2**n )")
print("c) f4 has the big O as O(ln n)")

# Ex 2

# a)

def swap2(liste, p1, p2):
    liste[p1], liste[p2] = liste[p2], liste[p1]

def find_max2(liste, p1, p2):
    sublist = liste[p1:p2 + 1]
    return p1 + sublist.index(max(sublist))

def random_list2(n, min, max):
    return [random.randint(min, max) for _ in range(n)]

def separate_list(L, index):
    return L[:index], L[index], L[index+1:]


# algorithme de tri

def selection_sort(L):
    for bottom_pos in range(len(L)):
    max_index = find_max2(L, bottom_pos, len(L) - 1)
    swap(L, max_index, bottom_pos)


def bubble_sort2(l):
    length = len(l)
    for i in range(1, length):
        sorted = True
        for j in range(length - i):
            if l[j] < l[j + 1]:
             swap(l, j, j + 1)
             sorted = False

        if sorted: # it can happen that we don't need to do all the loops
            return

def insertion_sort(L):
    i = 1
    while i < len(L):
        j = i
        while j > 0 and L[j-1] < L[j]:
            swap(L, j, j-1)
            j = j - 1
        i = i + 1