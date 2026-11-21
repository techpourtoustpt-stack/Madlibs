print("__________________________")
print("Welcome to madlibs world !")
print()
print("a madlib is a standar template of sentence with gaps inside of it to fill with indormations from the user.")
print()
print("Player 1: ")

madlib = input("enter your madlib: ")

countwords = 0
for ch in madlib:
    if ch == '_':
        countwords += 1

if countwords == 0:
    print("usage : [Hello _, my name is _.]")
else:
    madliblist = madlib.split('_')
    for i in range(countwords):
        word = input(f"Enter word {i + 1} :")
        madliblist.insert(2*i + 1, word)

for string in madliblist:
    print(string, end=" ")

print()
