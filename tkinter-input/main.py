#
# ########################### -------- EXAMPLE OF CREATING SPACE
#
# from tkinter import *
#
# window = Tk()
#
# r = Label(bg ="red", width="20", height=5)
# r.grid(row=0, column=0)
#
#
# g = Label(bg ="green", width="20", height=5)
# g.grid(row=1, column=1)
#
#
# b = Label(bg ="blue", width="40", height=5)
# b.grid(row=2, column=0,columnspan=2)
#
# window.mainloop()

########################### -------- input / output

from tkinter import *

window = Tk()
window.title("Example of input/output")
window.config(padx = 20, pady = 20)

canvas = Canvas(height=200, width = 200)
logo = PhotoImage(file="in-out.jpg")
canvas.create_image(100,100, image = logo)
canvas.grid(row=0, column=1)


