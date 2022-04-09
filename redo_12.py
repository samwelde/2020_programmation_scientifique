

# Ex 1

wList = []

def initStack():
    global wList
    wList =  []

def isEmpty():
    global wList
    if len(wList) ==0:
        return True
    else:
        return False

def push():
    global wList
    wList.append(x)

#print(push(1))

def pop():
    global wList
    return wList.pop()

def top():
    global wList
    return wList[-1]

def size():
    global wList
    return len(wList)

# b)

# c)

def isOpeningSymbol(c):
    if c == "(" or c == "{" or c == "[":
        return True
    else:
        return False

def isClosingSymbol(c):
    if c == ")" or c == "}" or c == "]":
        return True
    else:
        return False

def isMatchingSymbol(c1, c2):
    if c1 == "(" and c2 == ")":
        return True
    elif c1 == "{" and c2 == "}":
        return True
    elif c1 == "[" and c2 == "]":
        return True
    else:
        return False


def isBalanced(expression=""):
    initStack()
    for char in expression:
        if isOpeningSymbol(char):
            push(char)
        elif isClosingSymbol(char):
            if isEmpty():
                return False
            elif not isMatchingSymbol(pop(), char):
                return False
    return isEmpty()

# d)
def f(w):
    r = ""
    initStack()
    for i in range (len(w)):
        push(w[i])
    while not isEmpty():
        r = r + pop()
    return r
print("d) f(w) is 1) adding every caractere in w to the pile and...")
print(" 2) will return one new word with every letter from pile")

def g(e):
    r = ""
    while not isEmpty() and top() != e:
        r = r+pop()
        for i in r:
            push(i)

print(" d) g(w) is reversing part of the pile with characteres of e")
print(" a-e is ok but then e,f,g,h gets reversed placed in pile")


# Ex 2

# a)
wList = []

def initQueue():
    global wList
    wList = []

def isEmpty():
    if len(wList) ==0:
        return True

def enqueue(x):
    global wList
    whilst.append(x)

def dequeue():
    global wList
    return wList.pop(0)

def consult():
    global wList
    return wList[0]

def size():
    global wList
    return len(wList)

# c)
def h(e):
    s = size()
    for i in range(s):
        c = dequeue()
        if not c==e:
            enqueue()
print("c) h(e) is a fct which will")
print("remove all caracteres similar to e from file s")

# Ex 3
# a)

wList = []

def initSet():
    global wList
    wList = []

def isEmpty():
    global wList
    if len(wList)==0:
        return True
    else:
        return False

def add(x):
    global wList
    if not contains(x):
        wList.append(x)

def remove(x):
    global wList
    if contains(x):
        for i,e in enumerate(wList):    # numeriert Elemente
            if e == x:
                del wList[i]
                break

def contains(x):
    global wList
    for e in wList:
        if e == x:
            return True
    return False

def size():
    global wList
    return len(wList)

# c)
print("Complexité de...")
print("- add(x) = O(n)")
print("- remove(x) = O(n)")
print("- contains(x) = O(n)")
print()
# d)
print("ensemble(set) != multi occurrence!")
print()

# Ex 4

# a)

def countWords(sentence):
    dic = {}
    sentence_split = sentence.lower().split(" ")
    for word in sentence_split:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic

print(countWords("I would not like them Here or there I would not like them Anywhere I do not like Green eggs and ham"))
print()

# b)

def translate(phrase, dictionary):
    translation = ""
    for word in phrase.split(" "):
        if word in dictionary.keys():
            translation += dictionary[word]
        else:
            translation += word
        translation += " "
    return translation

dictionary= {
    "loves": "aime",
    "pineapple": "ananas",
    "cats": "chats",
    "and": "et",
    "or": "ou"}

phrase = "Jane loves pineapple and cats"
print(translate(phrase, dictionary))