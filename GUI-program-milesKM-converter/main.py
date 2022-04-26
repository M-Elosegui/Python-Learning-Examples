###### BASIC SETUPS EXAMPLES

#
# from tkinter import *
#
# #Window
# window = Tk()
# window.title("My 1st program")
# window.minsize(width=500, height=400)
#
#
# #Label
# mylabel = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# mylabel["text"] = "Next Text"
# mylabel.config(text="New Text")
# mylabel.grid(column=0, row=0)
#
#
# #Button
# def button_clicked():
#     print("I got clicked")
#     text = input.get()
#     mylabel.config(text=text)
#
# def button_clickedV2():
#     pass
#
# button = Button(text = "click me", command=button_clicked)
# button.grid(column=1, row=1)
#
# button2 = Button(text = "Second one")
# button.grid(column=2, row=2)
#
# #Entry
# input = Entry(width=10)
# input.grid(column=3, row=3)
# print(input.get())
#
#
# window.mainloop()


############# WORKING CONVERTER

from tkinter import *

def milesKM():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0 )

miles_label = Label(text="Miles")
miles_label.grid(column=2 , row=0 )

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0 , row=1 )

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1 , row=1 )

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2 , row=1 )

kilometer_button = Button(text="Calculate", command=milesKM)
kilometer_button.grid(column=1 , row=2 )


window.mainloop()

