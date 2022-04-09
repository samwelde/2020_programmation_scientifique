from tkinter import *

symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def get_symbol(value):
	"""
	Retourne le symbole associé à la valeur passée en paramètre
	"""
	global symbols
	return symbols[value]


def get_value(symbol):
	"""
	Retourne la valeur numérique du symbole passé en paramètre
	"""
	global symbols
	return symbols.index(symbol)


def repr_to_value(b, x):
	"""
	Prend en paramètre une base (int) et une chaîne de charactères qui représente un nombre et le convertit en entierW
	"""
	res = 0
	if len(x) > 0:
		reversed_string = x[::-1]
		for i, c in enumerate(reversed_string):
			res += get_value(c) * b ** i
	return res


def value_to_repr(b, x):
	"""
	Prend en paramètre une base (int) et une valeur (int) et renvoie une chaîtne de charactère représentant x dans la base b.
	"""
	if x == 0:
		return "0"
	res = ""
	while not(x == 0):
		res += get_symbol(x % b)
		x = x // b

	return "".join(res)[::-1]


def convert_from_base_to_base():
	"""
	Utilise les fonctions ci-dessus pour opérer un changement de base sur les variable tkinter. Il sera effectué
	lorsqu'on appuie sur le bouton pour convertir
	"""
	value = repr_to_value(input_base.get(), input_value.get())
	representation_in_new_base = value_to_repr(output_base.get(), value)
	output.set(representation_in_new_base)


window = Tk()
window.grid_columnconfigure(1, weight=1)

input_value = StringVar()
input_value.set("456")

output = IntVar()

input_base = IntVar()
input_base.set(10)

output_base = IntVar()
output_base.set(2)

window.title("Welcome to the number converter")

# label pour la valeur à convertir
valueLbl = Label(window, text="Value to convert: ")
valueLbl.grid(column=0, row=0, sticky="E")
# champ de texte pour écrire la valeur
value_to_convert_entry = Entry(window, width=20, textvariable=input_value)
value_to_convert_entry.grid(column=1, row=0, sticky = "EW")

# label pour la base d'origine
origin_base_lbl = Label(window, text="Origin base: ")
origin_base_lbl.grid(column=0, row=1, sticky="E")
# champ de texte pour la base d'origine
origin_base_entry = Entry(window, width=20, textvariable=input_base)
origin_base_entry.grid(column=1, row=1, sticky = "EW")

# label pour la base d'arrivée
target_base_lbl = Label(window, text="Target base: ")
target_base_lbl.grid(column=0, row=2, sticky="E")
# champ de texte pour la base d'arrivée
target_base_entry = Entry(window, width=20, textvariable=output_base)
target_base_entry.grid(column=1, row=2, sticky = "EW")

# label pour le résultat
answerLbl = Label(window, text="Result: ")
answerLbl.grid(column=0, row=3, sticky="E")
# champ de texte non modifiable pour afficher le résultat
answer = Entry(window, width=20, state="readonly", textvariable=output)
answer.grid(column=1, row=3, sticky = "EW")

# Bouton qui lance la conversion
convertButton = Button(window, text="Convert !", command=convert_from_base_to_base)
convertButton.grid(column=0, row=4, columnspan=2, sticky="EW")

window.mainloop()
