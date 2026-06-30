# Word Counter from Text File

filename = input("Enter the file name: ")

try:
    file = open(filename, "r")

    text = file.read()

    print("\n------File Content------")
    print(text)
    print("-------------------------")

    lines = text.split("\n")
    words = text.split()

    print("\n------File Statistics------")
    print("Number of Lines      :", len(lines))
    print("Number of Words      :", len(words))
    print("Number of Characters :", len(text))
    print("----------------------------")

    file.close()

except FileNotFoundError:
    print("File not found!")