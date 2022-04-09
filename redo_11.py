


#Ex 1
# a)

voyelles = 'aeiouy'

def transform(s):
    transformed_s = ''
    for char in s:
        if char in voyelles:
            transformed_s += char
        else:
            transformed_s += char.upper()
    return transformed_s

s = ["b","o","n","j","o","u","r"]

#print(transform(s))
#print(transform("bonjour"))

# b)
#test = input("Entrez une phrase au clavier:", )
#print(test)
#print(transform(test))
# wrong

s = ''
#while s != "stop":
    #s = input("Entrez une phrase au clavier: ")
    #print(transform(s))


# 2

import random

# a)
S = [x**3 for x in range(0,22,2)]
#print(S)

# b)
V = [2 **i for i in range(13)]

# c)
M = [ x for x in S if x &3 ==0]

# d)
R = [random.randint(-20,20)**3 for _ in range(10)]

# e)
l = [elem for elem in R if elem < 0]

# f)
words = ["Voici", "des", "Mots"]

l = [word[0].lower() for word in words]
print(l)

# g)
l = [list(word) for word in words]
print(l)

# h)
L1 = [1,2,3]
L2 = [4,5,6]
L3 = [L1[i] + L2[i] for i in range(len(L1))]
print(L3)



# Ex 3

my_list = [8, 2, 4, 1, 7, 3, 9, 14, -1]

def my_sort(L):
    if not L:
        return []

    pivot = L[0]
    tail = L[1:]

    L1 = [n for n in tail if n < pivot]
    L2 = [n for n in tail if n >= pivot]

    return my_sort(L1) + [pivot] + my_sort(L2)

#print(my_sort(my_list))


# Ex 4

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def decode(m, n):
    decoded_message = ''

    for word in m.split():
        reversed_word = word[::-1]
        decoded_word = ''

        for char in reversed_word:
            index_in_alphabet = alphabet.index(char)
            shifted_char = alphabet[(index_in_alphabet + n) % len(alphabet)]
            decoded_word += shifted_char

        decoded_message += decoded_word + ' '

    return decoded_message
print(decode(alphabet, 3))

encoded_message = "av rug zbqtavx sb rug qavyo rug rab qrlr anz fv tavx"

for n in range(1,27):
    print("{:>2}: {}".format(n, decode(encoded_message, n)))


# Ex 5
# a)
import numpy as np
import matplotlib.pylab as plt
import matplotlib.patches as mpatches #for legends

data = np.loadtxt("11_PS20-S11-ex.csv", delimiter=",",
            dtype={"names":["Pays", "Region", "Surface", "Population", "PNB", "Exports","Imports"],
            "formats":["U20", "U20", "i4", "i4", "i4", "i4", "i4"]},
            skiprows=1)
print()

# b)
for i in range(0, data.size):
    print(i,data["Pays"][i], data["Population"][i])

print()

# c)
max_surface_country = data['Pays'][np.argmax(data['Surface'])]
min_surface_country = data['Pays'][np.argmin(data['Surface'])]
print(" Country with biggest surface:", max_surface_country)
print("Country with smallest surface:", min_surface_country)

# d) missing from here on

plt.hist(data["Population"], bins=100)
mean = data['Population'].mean()
median = np.median(data['Population'])
red_patch = mpatches.Patch(color='red', label='Moyenne:{:.2f}'.format(mean))
green_patch = mpatches.Patch(color='green', label='Mediane:{:.2f}'.format(median))
plt.figlegend(handles=[red_patch, green_patch], loc='upper center', ncol=2)
plt.axvline(mean, c='red')
plt.axvline(median, c='green')
plt.xlabel("population")
plt.ylabel("#countries")
plt.show()

# e)

density = data['Population']*1.0/data['Surface']
plt.hist(density, bins=50)
plt.xlabel('habitants/km2')
plt.ylabel('#countries')
plt.text(3, 80, 'densité maximum: {:.2f}'.format(np.amax(density)))
plt.text(3, 60, 'densité minimum: {:.6f}'.format(np.amin(density)))
plt.show()

# f)

asiaPNBDensity = []
europaPNBDensity = []
  #  for i in range(0, data.size):
   #     if data["Region"][i] == "Asien":
    #        asiaPNBDensity.append(data["Population"][i] * 1.0 / data["Surface"][i])
     #   elif data["Region"][i] == "Naher Osten":
      #      europaPNBDensity.append(data["Population"][i] * 1.0 / data["Surface"][i])

plt.hist(asiaPNBDensity, label='Asien', alpha=0.5, bins=30)
plt.hist(europaPNBDensity, label='Naher Osten', bins=10)

plt.xlabel('habitants/km2')
plt.ylabel('#countries')
plt.legend()
plt.show()




def mystery(a, b):
    print("a:", a)
    print("b:", b)
    if (b == 0):
        return 0
    if (b % 2 == 0):
        return mystery(a+a, b//2)
    return mystery(a+a, b//2) + a

for i in (1, 10):
    for j in (1,10):
        print("here: ",mystery(i, j))



print(bin(13))