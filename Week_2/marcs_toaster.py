loaf = ["bread", "bread", "bread", "tv remote"]
spreads = ["Jam", "Cheese", "chocolate", "butter"]

def toaster(top_hole):
    result = None

    if top_hole == "bread":
        result = "toast"
    else:
        result = "burnt"
    return result

def spreader(spred, toast, sprinkles=False):
    if sprinkles:
        print(f"{toast} with {spred} and sprinkles")
    else:
        print(f"{toast} with {spred}")

loaf_qty = len(loaf)
index = 0

while index < loaf_qty:
    result = toaster(loaf[index])
    spreader(spreads[index] ,result, True)
    index +=1


# sum_integers_args.py
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
        
    return result

print(my_sum(1, 2, 3, 4, 1, 1, 1))
