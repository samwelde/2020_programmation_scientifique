
# Example
#############
a = 60
b = 13
c = 0

c = a&b
print("Line 1 - Value of c is ", c)
# 12 because
# 60 = 0011 1100
# 13 = 0000 1101
# a&b= 0000 1100

c = a | b
print("Line 2 - Value of c is ", c)
# 61 because
# 60 = 0011 1100
# 13 = 0000 1101
# a|b= 0011 1101

c = a ^ b
print("Line 3 - Value of c is ", c)
# 49 because
# 60 = 0011 1100
# 13 = 0000 1101
# a^b= 0011 0001

c = ~a
print("Line 4 - Value of c is ", c)
# -61 because
# 60 = 0011 1100
# ~a = 1100 0011

c = a << 2
print("Line 5 - Value of c is ", c)
# 240 because
# 60 = 0011 1100
#a<<2= 1111 0000

c = a >> 2
print("Line 5 - Value of c is ", c)
print()
# 15 because
# 60 = 0011 1100
#a>>2= 0000 1111

#######################


# Ex 1
# Conversion of binaire, décimal and hexadécimal

# Ex 2
# a)
import datetime

s = 2147483647
# int of 32bits = 2147483647 negative and positive numbers

m, s_r = divmod(s, 60)
h, m_r = divmod(m, 60)
d, h_r = divmod(h, 24)
y, d_r = divmod(d, 365.25)
# divmod() method takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.

print("Max time, 32bits can show is", y, "years", d_r, "days", h_r, "hours", m_r, "minutes", s_r, "seconds")

initial_date = datetime.datetime(1970, 1,1,0,0,0,)
problematic_date = datetime.datetime(1970 + int(y), 1, 1 + int(d_r), h_r, m_r, s_r)

print("initial POSIX date:", initial_date)
print("maximal POSIX date:", problematic_date)
print()


# Ex 4
# a)
import numpy as np

def decToBin(v):
    bin_val = ""
    m = v
    while m > 0:
        m,r = divmod(m,2)
        bin_val = str(r) + bin_val
    return bin_val

decVal = 14
binVal = decToBin(decVal)

print("a) val =", decVal)
print("a) bin =", binVal)
print()


# b)
def binToDec(b):
    exponent = len(b) -1
    dec_value = 0
    for char in b:
        if char == "1":
            dec_value += 2 ** exponent
        exponent -= 1
    return dec_value

decVal = binToDec(binVal)
print("b) val =", decVal)