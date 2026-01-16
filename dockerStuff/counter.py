# opens a file and increments the value by 1 each time this is run

try:
    with open("/counts/count.txt", "r+") as f:
        contents = int(f.read().strip())
        contents += 1
        f.seek(0)
        f.truncate()
        print(contents, file=f)
        print(f"The count is {contents}")
except FileNotFoundError:
    with open("/counts/count.txt", "w") as f:
        print(1, file=f)
        print(f"The count is 1")
