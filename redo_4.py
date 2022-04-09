import ax as ax
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as plt3d
import csv
#Ex 1
#a)

#t = [0 , 4*np.pi]
t = np.linspace(0 , 4*np.pi,1000)

x = t*np.cos(t)
y = t*np.sin(t)

plt.title("Ex1 a) Spirale d'Archimède")

plt.xlabel("x")
plt.ylabel("y")

plt.xlim(-10,15)
plt.ylim(-15,10)

#plt.plot(x,y)
#plt.show()

#b)

t = np.linspace(0 , 4*np.pi,1000)

x = t*np.cos(t)
y = t*np.sin(t)
a = 1
z = a*t

plt.title("Ex1 b) Spirale d'Archimède en 3D")
ax = plt3d.Axes3D(plt.figure())

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.set_xlim(-10,15)
ax.set_ylim(-15,10)
ax.set_zlim(0,14)
#or
#plt.axis("equal")

ax.plot(x,y,z)
#plt.show()
#print()

#Ex 2
#a)

temperature = np.loadtxt("temperatures.txt")
#print("a)", temperature)

#b)
heures = np.arange(0,24,0.5)
#or
#heures = np.linspace(0,23.5,len(temperatures))

#print("b)", heures)

#c)

subplot1 = plt.subplot(1,2,1)

plt.title("Evolution de la température sur une journée")

plt.xlabel("heure")
plt.ylabel("Degrés")

plt.xlim(0,25)
plt.ylim(0,8)

plt.plot(heures, temperature, 'b--')
#plt.show()

#d)
subplot2 = plt.subplot(1,2,2)

plt.title("")

plt.xlabel("heure")
plt.ylabel("degrés")

plt.xlim(0,25)
plt.ylim(0,8)

plt.scatter(heures, temperature, c=temperature, cmap="winter", marker="s")

plt.plot(heures, temperature)   #'go', 'r--', 'b-'
#plt.show()


#Ex 3
#a)

brain_file = open('brain.csv', 'r')
csv_reader = csv.reader(brain_file)
data = np.array(list(csv_reader), dtype=float)
brain_file.close()

#b)
brain_weights = data[:, 2]
brain_sizes = data[:, 3]

plt.subplot(221)
plt.hist(brain_sizes, edgecolor='black', bins=20)
plt.title("Histrogram of brain weights")
plt.xlabel("Brain weights (gr)")
plt.ylabel("Counts")

plt.subplot(222)
plt.hist(brain_weights, edgecolor='black', bins=20)
plt.title("Histrogram of brain sizes")
plt.xlabel("Brain sizes (cm3)")
plt.ylabel("Counts")

plt.subplot(212)

#print(brain_weights.size)
#print(brain_sizes.size)

plt.scatter(brain_weights, brain_sizes)
plt.title('Head size as a function of brain weight')
plt.xlabel('Brain weight (g)')
plt.ylabel('Brain size ($cm^3$)')

#plt.show()


# Ex 4
#a)

bio_file = open("bio_signal.csv", "r")
csv_reader = csv.reader(bio_file)
data = np.array(list(csv_reader), dtype=float)

bio_data_one = data[0]
bio_file.close()

#b)
middle = len(bio_data_one)//2

pos1 = np.argmax(bio_data_one[:middle])
#print(pos1)

pos2 = middle + np.argmax(bio_data_one[middle:])
#print(pos2)


#c)
x = np.linspace(0,1000,len(bio_data_one))

plt.plot(x, bio_data_one)

plt.axvline(pos1, color="red")
plt.axvline(pos2, color="green")

plt.xlabel("time")
plt.ylabel("ECG Reading")

plt.show()

#d)
sampl_freq = 500
print(60/ ((float)(pos2-pos1) / sampl_freq))

#Ex 5

a = 2
b = 0.3

u = np.linspace(0, 2*np.pi, nbrPoints)
v = np.linspace(0.01, 2, nbrPoints)

x = a * np.cos(u) * np.sin(v)
y = a * np.sin(u) * np.sin(v)
z = a(np.cos(v) + np.log(np.tan(v/2)) + b*u)

ax = plt3d.Axes3D(plt.figure())
plt.plot(x,y,z)
plt.show()

