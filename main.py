import tkinter as tk 
from tkinter import TRUE, Listbox, messagebox
import random
import string



# global variables
students = [{"username": "t1s1", "password": "t1password","first_name": "t1", "last_name": "s1", "email": "t1@s1", "section": "A"}, {"username": "t2s2", "password": "t2password","first_name": "t2", "last_name": "s2", "email": "t2@s2", "section": "B"}] 


teachers = [{"username": "t1", "password": "teacher1"}, {"username": "t2", "password": "teacher2"}]

def show_class(section):
  
  # create a new window for teacher homepage
  class_page = tk.Toplevel(window)
  class_page.lift()
  class_page.title("Class " + section)
  
  # set dimensions
  window_width = 500
  window_height = 500
  class_page.geometry(f"{window_width}x{window_height}")


  list_box = tk.Listbox(class_page, selectmode=tk.MULTIPLE)
  list_box.pack(fill=tk.BOTH, expand=TRUE)

  #list_box.insert(tk.END, "FIRST NAME    LAST NAME    SECTION" )

  for value in students:
    if value['section'] == section:
        list_box.insert(tk.END, value['first_name'] + " " + value['last_name'] + "  --->  " + value['section'])

def t_sign_out(teacher_home_page):
  teacher_home_page.destroy()
  entry_username.delete(0, tk.END)
  entry_password.delete(0, tk.END)

def teacher_login():
  # create a new window for teacher homepage
  teacher_home_page = tk.Toplevel(window)
  teacher_home_page.title("Teacher Homepage")

  # set dimensions
  window_width = 500
  window_height = 500
  teacher_home_page.geometry(f"{window_width}x{window_height}")

  btn_A = tk.Button(teacher_home_page, text="A", command=lambda: show_class("A"), width=5, height=2 )
  btn_A.pack(padx=10, pady=10)
  btn_B = tk.Button(teacher_home_page, text="B", command=lambda: show_class("B"), width=5, height=2 )
  btn_B.pack(padx=10, pady=10)
  btn_sign_out = tk.Button(teacher_home_page, text="Sign Out", command=lambda: t_sign_out(teacher_home_page), width=5, height=2 )
  btn_sign_out.pack(padx=10, pady=10)

  
  

# defining login and sign_up functions
def login():
  username = entry_username.get()
  password = entry_password.get()
  login_successful = False

  for detail in teachers:
    if detail['username'] == username and detail['password'] == password:
      messagebox.showinfo("Correct details")
      login_successful = True
      teacher_login()

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

  
  def section_generator():
    random_float = random.random()

    # it generates a value within 1 and 0
    if random_float > 0.5:
      return "A"
    else:
      return "B"

  
  def register():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    username = (first_name[0:3] + last_name[0:3]).lower()
    password = generate_random_password()
    section = section_generator()
    print(f"Username: {username}\nPassword:{password}\nSection:{section}")
    students.append({"username": username, "password": password,"first_name": first_name, "last_name": last_name, "email": email, "section": section})
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
label_username.pack(padx=10, pady=10) # adding to the box


entry_username = tk.Entry(window)
entry_username.pack(padx=10, pady=10)

label_password = tk.Label(window, text="Password:")  # creating the title for the textbox
label_password.pack(padx=10, pady=10) # adding to the box

entry_password = tk.Entry(window, show="*")
entry_password.pack(padx=10, pady=10)


# create a login and sign up button
btn_login = tk.Button(window, text="Login", command=login)
btn_login.pack(padx=10, pady=10)

btn_sign_up = tk.Button(window, text="Sign Up", command=sign_up)
btn_sign_up.pack(padx=10, pady=10)


window.mainloop()
