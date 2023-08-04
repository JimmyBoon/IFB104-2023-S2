b_animals = ["bear", "bull", "bee"]

zoo = []

for animal in b_animals:
    zoo.append(animal)
    print(animal + " has been added to the zoo")

zoo.append("bat")
print(f"The zoo contains: {zoo}")
print(f"The b_animals are: {b_animals}")


counter = 100


while True:

    counter -= 1
    if counter % 2 == 0:
        continue
    
    print(f"The counter is: {counter}")

    if counter == 59:
        print("The loop is broken")
        break

    

