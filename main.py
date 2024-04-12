import tkinter as tk 
# from tkinter import messagebox





# create a main window
window = tk.Tk()  # creating a window using tk
window.title("Login Form")

# create labels
label_username = tk.Label(window, text="Username:")  # creating the title for the textbox
label_username.pack() # adding to the box


entry_username = tk.Entry(window)
entry_username.pack()

label_password = tk.Label(window, text="Password:")  # creating the title for the textbox
label_password.pack() # adding to the box

entry_password = tk.Entry(window, show="*")
entry_password.pack()


# create a login button


window.mainloop()