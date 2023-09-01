my_list = ["One", "two", "three", "four"]

# file1 = open("my_demo_file.txt", "w")

# for word in my_list:
    
#     file1.write(word + "\n")

# file1.close()

with open("my_demo_file.txt", "w") as file:
    for word in my_list:
        file.write(word + "\n")