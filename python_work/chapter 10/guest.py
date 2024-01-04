from pathlib import Path

name = input("What is your name? ")

path = Path("guest.txt")
path.write_text(name)

names = []

while True:
    name = input("What is your name? ")

    if name == "q":
        break

    names.append(name) 

path = Path("guest_book.txt")
path.write_text(str.join("\n", names))