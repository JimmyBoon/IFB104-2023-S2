from termcolor import colored


def my_func(am_pm_eve, name, colour="green"):
    

    if am_pm_eve == "pm":
        time_word = "Afternoon"
    elif am_pm_eve == "eve":
        time_word = "Evening"
    elif am_pm_eve == "am":
        time_word = "Morning"
    else:
        time_word = "Day"
    
    text = colored(f"Good {time_word} {name}", colour)

    print(text)
    
    
    return "Good bye"



print(my_func(5, "James", "blue"))
