loaf = ["bread", "bread", "bread", "tv remote"]


def toaster(top_hole):

    result = None

    
    if top_hole == "bread":
        result = "toast"
    else:
        result = "burnt"


    return result


def toaster_recursive(loaf, i):
    
    if i < len(loaf):
        print(toaster(loaf[i]))
        toaster_recursive(loaf, i+1)
    else:
        return

toaster_recursive(loaf, 0)
