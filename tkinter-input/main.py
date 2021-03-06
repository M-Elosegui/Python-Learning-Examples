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
from PIL import Image, ImageTk
from tkinter import messagebox
import CodeGen
import json


# FUNCTIONS:

# def passwrite():
#     password_label.insert(END,"pass1.segura2.e3.boa4")
#     wordipass = password_label.get()
#     print (wordipass)

def search():
    with open("data1.json", "r") as data_file_jason:
        try:
            data = json.load(data_file_jason)
            search_key = website_entry.get()
            result = data[search_key]
            temp_mail = result["email"]
            temp_pass = result["password"]
            messagebox.showinfo(title=search_key,
                                message=f"Your email:  {temp_mail} \nYour password:  {temp_pass}")
        except KeyError:
            messagebox.showinfo(title="Not Found!",
                                message=f" Sorry, the website you're looking for is not in our database.")


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops! Blank field", message="Please make sure you haven't left any fields empty.")

    else:

        is_ok = messagebox.askokcancel(title="website",
                                       message=f"SUCCESS! \n These are the details you entered: \n \n Website:  {website} \n Email:  {email} \n Password:  {password} ")
        if is_ok:

            try:
                with open("data1.json", "r") as data_file_jason:
                    data = json.load(data_file_jason)
                # data.update(new_data)

            except FileNotFoundError:
                with open("data1.json", "w") as data_file_jason:
                    json.dump(new_data, data_file_jason, indent=4)

            else:
                data.update(new_data)

                with open("data1.json", "w") as data_file_jason:
                    json.dump(data, data_file_jason, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

            ### To open an existing one
            # with open("data1.json", "w") as data_file_jason:
            #     json.dump(new_data, data_file_jason, indent=4)
            #     data = jsonload(data_file_jason)
            #     json.update(new_data)
            #     json.dump(data, data_file_jason, indent=4)

        ###             BLOCK WITH .txt format
        # if is_ok:
        #     with open("data.txt","a") as data_file:
        #         data_file.write(f" {website} | {email} | {password} \n")
        #         website_entry.delete(0,END)
        #         password_entry.delete(0,END)
        #


# UI SETUP

window = Tk()
window.title("Example of input/output")
window.config(padx=20, pady=20)
canvas = Canvas(height=400, width=400)

# Image resized with PIL commands
img = Image.open("in-out.jpg")
img_resized = img.resize((300, 300), Image.ANTIALIAS)
new_img = ImageTk.PhotoImage(img_resized)

# logo = PhotoImage(file="in-out.jpg")
canvas.create_image(200, 200, image=new_img)
canvas.grid(row=0, column=1)

# Labels (text)
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries (entry fields)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "example@mail.inserted")
password_entry = Entry(width=15)
password_entry.grid(row=3, column=1, columnspan=2)


# Buttons

def thingtemp():
    password_entry.delete(0, END)
    little_pass = CodeGen.pass_gen()
    password_entry.insert(0, little_pass)


pass_gen_button = Button(text="Gen Pass", command=thingtemp)
pass_gen_button.grid(row=3, column=4)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2)

window.mainloop()

### OTHER
# from PIL import Image, ImageTk

# image1 = Image.open('aqua.png')
# image1.putalpha(128)
# image1 = image1.resize((image1.width//5,image1.height//5))
# gif1 = ImageTk.PhotoImage(image1)
