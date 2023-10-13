
# file = open("demo.txt")
# contents = file.read()
# print(contents)

# file.close

with open("demo.txt") as file:
    contents = file.read()
    print(contents)

    