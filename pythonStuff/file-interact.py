# interacts with notes file

note = input("Enter your note: ")

with open("notes.txt", "a") as f:
    print(note, file=f)

with open("notes.txt", "r") as file:
    contents = file.read()
    print(contents)

