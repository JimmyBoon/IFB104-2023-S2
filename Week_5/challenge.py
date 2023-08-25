# Week 5 challenge
# Make a function that takes the shopping list and cash.
# The function should return the items it can buy with the cash as well as the change left.

shopping_list = [("bread",3.5), ("milk",3.25), ("chicken",13.35), ("chocolate",5.75), ("ceral",6.25), ("pasta",0.60), ("veggies",2.5)]
cash = 19.50

# itemsICanBuy = []

# for item, cost in shopping_list:

#     if cost <= cash:
#         itemsICanBuy.append(item)
#         cash -= cost

# #print(itemsICanBuy)  
# print("I can buy " + str(itemsICanBuy) + " and have $" + str(cash) + " left.")

def go_shopping(my_shopping_list, money):
    itemsICanBuy = []

    for item, cost in my_shopping_list:
        if cost <= money:
            itemsICanBuy.append(item)
            money -= cost
    
    return itemsICanBuy, money

stuff, change = go_shopping(shopping_list, cash)

for item in stuff:
    if(item == "chocolate"):
        print(f"I am going to throw the {item} out")
    else:
        print(f"The thing I bought {item} and it is healthy")

