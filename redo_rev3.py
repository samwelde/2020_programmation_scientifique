from tkinter import *
from tkinter.scrolledtext import ScrolledText

'''
Solution to the theoretical question: Can you use only one dictionary ?
The answer is no, as you can only get values by a given key, not the other way
around (unless you go through every entry which would be inefficient (O(n) vs
O(1) when searching by key). Furthermore you can not have two identical keys,
so in this use case, using two dictionaries is advised.
'''

dictioFrToGer = {
    'maison':'haus',
    'bouteille':'flasche',
    'chat':'katze'
}

dictioGerToFr = {
    'hund':'chien',
    'auto':'voiture',
}

def toFrench():
    textBoxFR.delete('1.0', END)
    DEtext = str(textBoxDE.get(1.0, END)).split()
    translation = ""
    for words in DEtext:
        print(words)
        # If not in the dictionary, do nothing
        try:
            translation += dictioGerToFr[words] + " "
        except KeyError:
            pass
    textBoxFR.insert(INSERT, translation)

def toGerman():
    textBoxDE.delete('1.0', END)
    FRtext = str(textBoxFR.get(1.0, END)).split()
    translation = ""
    for words in FRtext:
        print(words)
        try:
            translation += dictioFrToGer[words] + " "
        except KeyError:
            pass
    textBoxDE.insert(INSERT, translation)

root = Tk()
labelDE = Label(root, text="Deutsch").grid(row=0,column=0)
textBoxDE = ScrolledText(root)
textBoxDE.grid(row=1,column=0)

labelFR = Label(root, text="Français").grid(row=0,column=2)
textBoxFR = ScrolledText(root)
textBoxFR.grid(row=1,column=2)



btn_convert_to_fr = Button(root, text="> Convert to French> ", command=toFrench).grid(row=2,column=1)
btn_convert_to_ger = Button(root, text="< Convert to German< ", command=toGerman).grid(row=3,column=1)


root.mainloop()
