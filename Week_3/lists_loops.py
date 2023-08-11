my_list = ["String", 10, False, [1,2], ("What", "am", "I?"), {1:"One"}]

for item in my_list:
    print(item)

counter = 0

while counter < len(my_list):
    print(my_list[counter])

    if my_list[counter] == False:
        print("The Item was FALSE")

    counter += 1
