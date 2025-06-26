# import necessary libaries
from tkinter import date

# create window
root = Tk ()
root.title('Getting started with widgets')
root.geometry('400x300')

# Add widgets
# Add Label
lbl = Label(text="hey there!",fg="white",bg="#3895D3")
name_entry = Entry()

# Function to display a message
def display():

    # Read input given by user
    name = name_entry.get()

    #declayring a global variable
    # to make it accessibel any whare in the program global message
    message = "Welcome to the Application! /n Today's date is:"
    greet = "Hello"+name+"/n"

    # display details in a text box
    #specify where to add the details inside the text box
    text_box.insert(END, great)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
     