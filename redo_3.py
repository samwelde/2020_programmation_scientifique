import numpy as np
import matplotlib.pyplot as plt

#########
## Ex1 ##
#########

my_list = [13,93,22,7,13,44,77,13,62]
#1.1
#a)
print("a)",my_list[3])

#b)
print("b)", len(my_list))

#c)
print("c1)", my_list[-2])
#or
print("c2)", my_list[7])
#or
print("c3)", my_list[len(my_list)-2])

#d)
print("d1)", sorted(my_list, reverse=True))
#or
my_list.sort(reverse=True)
print("d2)", my_list)
print()

#a)
my_list[-5:]

print("a)", my_list[-5:], ", 5th last till the end")

#b)
my_list[-4:-2]
print("b)", my_list[-4:-2], ", 4th last till 2nd last")

#c)
my_list[::2]
print("c)", my_list[::2], ", complete list, every second")

#d)
my_list[len(my_list)-4]
print("d)", my_list[len(my_list)-4], ", only 4th last")

#e)
my_list.count(13)
print("e)", my_list.count(13), ", tell amount of 13 in my_list")
print()


#1.2
my_list0 = [16, 26, 36, 46, 56, 66, 76, 86, 96]

#a)
print("a)", list(range(16,106,10)))

#b)
print("b)", np.array(np.arange(16,106,10)))

#c)
print("c)", np.array(np.linspace(16,96,9)))
#list(range) with steps
#array(arange) with steps
#array(linspace) with n
print()

#1.3
my_list = [1, 2, 3]
my_array = np.array([1, 2, 3])

#a)
print("a1)", my_list + my_list)
print("a2)", my_array + my_array)
print("a1 = [123123] vs. a2 = [2,4,6]")

#b)
print("b1)", my_list * 4)
print("b2)", my_array * 4)
print("b1 = [123123123123] vs. b2 = [4,8,12]")
print()

#1.4
myArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
myMatrix1 = np.array([myArray[:3], myArray[3:6],myArray[6:9]])
print("1.41)", myMatrix1)
#or
print("1.42)",np.reshape(myArray,(3,3)))
#or
print("1.43)", np.array([[1,2,3], [4,5,6], [7,8,9]]))
print()

#1.5
data = np.array([[19, 28, 37],
                [46, 55, 64],
                [73, 82, 91]])

#a)
print("a1) x=", data[:,:2])
print("a2) y=", data[:,2:])

#b)
print("b1) u =", data[:2,:])
print("b2) v =", data[2:,:])

#c)
print("c) est déjà fait!")
print("c)", data[:,:2], data[:,2:])
print()

#Ex 2
#c)
x = np.array([0.5, 1.5, -3.0, 8, -1.5, np.pi])
x = np.clip(x, -3.5, 2.5)
print("c) np.clip leads to smaller data because of integral on the data", x)

#Ex 3
#only analysis and document what happend in the example

import numpy as np

print(’list manipulation’)

a = [[12,11,10,9], [8,7,6,5], [4,3,2,1]]
b = [a[1][1:4], a[2][1:4]]

print(’b =’, b)
print(’a[2][0]=’, a[2][0])

b[0][0] = 77

print(’b =’, b)
print(’a[0][0]=’, a[0][0])

print()

print(’array manipulation’)

a = np.array ([[12,11,10,9], [8,7,6,5], [4,3,2,1]])
b = a[1:3, 1:4]

print(’b =’, b)
print(’a[1][1]=’, a[1][1])

z[0][0] = 77

print(’b =’, b)
print(’a[0][0]=’, a[1][1])



#Ex 4


plt.title("Gaussian function with three coefficients", fontsize=16)

x = np.linspace(-10,10,1000)

k1 = 0.1
k2 = 1
k3 = 10

y1 = np.exp((-k1*x**2))
y2 = np.exp((-k2*x**2))
y3 = np.exp((-k3*x**2))

plt.plot(x,y1, label="k=0.1")
plt.plot(x,y2, label="k=1")
plt.plot(x,y3, label="k=10")

plt.legend()

plt.xlabel("x")
plt.ylabel("y=f(x)")

plt.show()
print()

#Ex 5

plt.title("Trident de Newton")
plt.legend(loc="lower left")

x = np.linspace(-3,3,100);

plt.plot(x, 1/x, color="orange", linewidth=1.7, linestyle="--", label="h(x) = 1/x")
plt.plot(x, x**2, color="magenta", linewidth=1.7, linestyle="--", label="g(x) = x^2")
plt.plot(x, x**2 +1/x, color="blue", linewidth=1.9, label="f(x) = x**2 + 1/x")

plt.xlim(-3,3)
plt.ylim(-10,10)

plt.show()

print(type("saml"))
print(hex(101))


# Ex 6
import imageio
import matplotlib.pyplot as plt
import numpy as np

img = imageio.imread('sponge-bob.jpg')
print(img.shape)

img_tinted = np.multiply(img, [0.8, 0.8, 0.8])
# Show the original image

plt.subplot(1, 2, 1)
plt.imshow(img)
# Show the tinted image

plt.subplot(1, 2, 2)
# A slight gotcha with imshow is that it might give strange results
# if presented with data that is not of type uint8.
# To work around this, we # explicitly cast the type of the values to uint8 before displaying it.
# plt.imshow(np.uint8(img_tinted))

img_tintedR = np.multiply(img_tinted, [1, 0, 0])
img_tintedG = np.multiply(img_tinted, [0, 1, 0])
img_tintedB = np.multiply(img_tinted, [0, 0, 1])

plt.subplot(1, 3, 1)
plt.imshow(np.uint8(img_tintedR))

plt.subplot(1, 3, 2)
plt.imshow(np.uint8(img_tintedG))

plt.subplot(1, 3, 3)
plt.imshow(np.uint8(img_tintedB))
plt.show()