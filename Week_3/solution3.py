animals = ["Fox", "Cow", "Cat", "Elephant", "Lion"]
foods = ["Chickens", "Grass", "Fish", "Plants", "Animals"]

#python list comprehension
#https://www.w3schools.com/python/python_lists_comprehension.asp


pairs = [(animals[i], foods[i]) for i in range(0, len(animals))]

lines = [print(f"The {pair[0]} eats {pair[1]}") for pair in pairs]