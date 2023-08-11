# 4! = 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2 * 1 = 120

# def factorial_rec(number):

#     if number == 1:
#         return 1
#     else:
#         return (number * factorial(number-1))
    
# print(factorial_rec(5))


def factorial_attempt(number):
    factorialList = []
    factorial = 1
    for step in range(number):
        factorialList.append(step + 1)
    
    print(f"factorialList: {factorialList}")

    multiplier = 1

    for number in range(len(factorialList)):
        multiplier = factorialList[number]
        factorial = factorial * multiplier
    return factorial
    
# print(factorial_attempt(5))

def factorial(number):

    result = 1

    for num in range(number):
        result *= num + 1
    
    return result

print(factorial(5))