import tkinter as tk 
from tkinter import messagebox
import random
import string



# global variables
students = []
teachers = [{"username": "t1", "password": "teacher1"}, {"username": "t2", "password": "teacher2"}]


# defining login and sign_up functions
def login():
  username = entry_username.get()
  password = entry_password.get()
  login_successful = False

  for detail in teachers:
    if detail['username'] == username and detail['password'] == password:
      messagebox.showinfo("Correct details")
      login_successful = True

  for detail in students:
    if detail['username'] == username and detail['password'] == password:
      messagebox.showinfo("Correct details")
      login_successful = True


  if not login_successful:
    messagebox.showerror("Login Unsuccessful")

    


def sign_up():
  def generate_random_password():
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(8))

    return password

  
  def register():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    username = first_name[0:3] + last_name[0:3]
    password = generate_random_password()
    print(f"{username} , {password}")
    students.append({"username": username, "password": password,"first_name": first_name, "last_name": last_name, "email": email})
    messagebox.showinfo("Registration Complete")
    registration_window.destroy()

  
  # create a new window for registration
  registration_window = tk.Toplevel(window)
  registration_window.title("Student Registration")

  # set dimensions
  window_width = 500
  window_height = 500
  registration_window.geometry(f"{window_width}x{window_height}")

  # labels
  label_first_name = tk.Label(registration_window, text="First Name: ")
  label_first_name.pack()

  entry_first_name = tk.Entry(registration_window)
  entry_first_name.pack()

  label_last_name = tk.Label(registration_window, text="Last Name: ")
  label_last_name.pack()

  entry_last_name = tk.Entry(registration_window)
  entry_last_name.pack()

  label_email = tk.Label(registration_window, text="Email: ")
  label_email.pack()

  entry_email = tk.Entry(registration_window)
  entry_email.pack()

  btn_register = tk.Button(registration_window, text="Register", command=register)
  btn_register.pack()

# create a main window
window = tk.Tk()  # creating a window using tk
window.title("Login Form")

# set dimensions
window_width = 500
window_height = 500
window.geometry(f"{window_width}x{window_height}")


# create labels
label_username = tk.Label(window, text="Username:")  # creating the title for the textbox
label_username.pack() # adding to the box


entry_username = tk.Entry(window)
entry_username.pack()

label_password = tk.Label(window, text="Password:")  # creating the title for the textbox
label_password.pack() # adding to the box

entry_password = tk.Entry(window, show="*")
entry_password.pack()


# create a login and sign up button
btn_login = tk.Button(window, text="Login", command=login)
btn_login.pack()

btn_sign_up = tk.Button(window, text="Sign Up", command=sign_up)
btn_sign_up.pack()


window.mainloop()