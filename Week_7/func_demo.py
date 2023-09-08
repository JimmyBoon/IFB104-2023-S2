my_zoo = [["Lion", "Steel", 100],
           ["Seal", "Pool", 14],
           ["Snake", "Glass Box", 88],
           ["Bear", "Woods", 77],
           ["Bird", "Wire", 3]]

def WhoIsWhoInTheZoo(zoo_things):
    
    for animal, cage, danger in zoo_things:
        print(f"The {animal} lives in the {cage} cage")

        if danger > 50:
            print(f"Be careful the {animal} is very dangerous")
        else:
            print(f"The {animal} will be happy to play with you")
    
        if animal == "Snake" or animal == "Bear":
            print("I am scared of snakes and bears")



WhoIsWhoInTheZoo(my_zoo)