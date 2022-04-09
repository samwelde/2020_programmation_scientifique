
# 08_PS
# Ex 5
print("5. L-systèmes et fractales")

import turtle

turtle.speed(0) # Vitesse maximale

# Déplace la tortue vers le coin inférieur gauche
turtle.penup()

turtle.setx(-turtle.window_width() * 0.45)
turtle.sety(-turtle.window_height() * 0.45)
turtle.pendown()
turtle.tracer(0, 0)

def apply_rules(S):
    string = ''
    for char in S:
        if char == 'A':
            string += 'B-A-B'
        elif char == 'B':
            string += 'A+B+A'
        else:
            string += char
    return string

def apply_rec(S, n):
    if n == 0:
        return S
    return apply_rec(apply_rules(S), n - 1)

def draw(S, length):
    for char in S:
        if char == 'A' or char == 'B':
            turtle.fd(length)
        elif char == '+':
            turtle.rt(60)
        elif char == '-':
            turtle.lt(60)

S = apply_rec("B", 8)
draw(S, 2)

turtle.update()
turtle.getcanvas().postscript(file="l_system.eps")
turtle.done()



# rev2
# Ex 1
print("1. L-systèmes avancés avec Turtle")

import turtle
turtle.speed(0)  # Vitesse maximale
# Déplace la tortue vers le bas
turtle.penup()
turtle.sety(-turtle.window_height() * 0.45)
turtle.left(90)
turtle.pendown()

rules1 = {
    "F": "FF",
    "X": "F[-X]+X"
}

rules2 = {
    "F": "FF",
    "X": "F-[[X]+X]+F[+FX]-X"
}

def apply_one(s,rules):
    if s in rules:
        return rules[s]
    else:
        return s

def apply_rules(S,rules):
    SS = [apply_one(s,rules) for s in S]
    return "".join(SS)

def apply(S, rules, n):
    for _ in range(n):
        S = apply_rules(S, rules)
    return S

def draw(S, angle, length):
    stack = []
    for c in S:
        if c == "F":
            turtle.fd(length)
        elif c == "+":
            turtle.rt(angle)
        elif c == "-":
            turtle.lt(angle)
        elif c == "[":
            state = get_state()
            stack.append(state)
        elif c =="]":
            state = stack.pop()
            set_state(state)

# not finished!


# Ex 2

def is_value_in_row(value, row):
    if value = sudoku[column]:
        return True
    else:
        return []

def is_value_in_column(value, colum):
    if value = sudoku[column]:
        return True
    else:
        return []

def is_sudoku_solved():
