# def my_decorator_func(func):

#     def wrapper_func():
#         # Do something before the function.
#         print("This is before")
#         func()
#         # Do something after the function.
#         print("This is after")

#     return wrapper_func


# @my_decorator_func
# def my_func():
#     print("I am a function")


# my_func()

import basic_math

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def walk_the_dog(self):
        print(f"{self.name} has enjoyed the walk")





dog = Dog("Buttons", "5", "Jack Russell")
dog1 = Dog("Mya", 3, "Bulldog")

dog_list = [dog, dog1]

for dog in dog_list:
    dog.walk_the_dog()

print(basic_math.sum(10,10))