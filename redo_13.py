# Ex 1
#


import tkinter as tk

win = tk.Tk()
win.grid()

text = tk.StringVar()
label = tk.Label(win, textvariable=text , anchor=’w’,
fg="white", bg="red", font=(None , 32))

label.grid(column=0, row=0, columnspan=10, sticky=’EW’)

def on_click(letter):
def f():
t = text.get() + letter
text.set(t)

return f

def on_ok():
t = text.get()
if t == "CAFE":
label.config(bg="green")
text.set("PASSWORD OK!")
else:
label.config(bg="red")
text.set("")

letters = ["A", "B", "C", "D", "E", "F"]
for i, letter in enumerate(letters):
button = tk.Button(win, text=letter , command=on_click(letter))
button.grid(column=i, row=1, sticky=’EW’)
win.grid_columnconfigure(i, weight=1)

button = tk.Button(win, text="OK", command=on_ok)
button.grid(column=0, row=2, columnspan=len(letters), sticky=’EW’)

tk.mainloop()