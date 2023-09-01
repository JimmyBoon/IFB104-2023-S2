from tkinter import Tk, Button

# Create a window
hello_window = Tk()

hello_window.title('Countdown')

name = "Ryan"
good_bye = False

def print_hello(name, good_bye):
    if good_bye:
        print(f"Good bye {name}")
    else:
        print(f"Hello {name}")

def toggle_good_bye():
    global good_bye
    good_bye = not good_bye
    print(good_bye)

the_greet_button = Button(hello_window, text = ' Push ',
                    font = ('Arial', 24), command = lambda : print_hello(name, good_bye))

the_greet_button.pack()

good_bye_toogle = Button(hello_window, text = " Toggle ", font = ('Arial', 24), command=toggle_good_bye)

good_bye_toogle.pack()

hello_window.mainloop()