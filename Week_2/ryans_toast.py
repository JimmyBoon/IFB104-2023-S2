#toast loaf in loaf with while loop
def toaster(topHole):

    result = None

    if topHole == "bread":
        result = "toast"
    else:
        result = "burnt"

    return result

loaf = ["bread", "bread", "bread", "tv remote"]

counter = 0

while counter < len(loaf):
    toastedThing = toaster(loaf[counter])
    print(f"When I toaste item {loaf[counter]} I get {toastedThing}")
    counter += 1
