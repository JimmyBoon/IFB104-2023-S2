
def toaster(top_hole):

    result = None

    
    if top_hole == "bread":
        result = "toast"
    else:
        result = "burnt"


    return result








loaf = ["bread", "bread", "bread", "tv remote"]

for i in range(0, len(loaf)):
    print(loaf[i])
    
#for piece in loaf:
#   toasted_thing = toaster(piece)
#   print(f"When I toast the {piece} I get {toasted_thing}")

for i in range(0, len(loaf)):
    toasted_thing = toaster(loaf[i])
    print(f"When I toast the item {i} of the loaf I get {toasted_thing}")


    
