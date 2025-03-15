import tkinter as tk
from tkinter import *
from tkinter import messagebox
from pymysql import connect, IntegrityError
from PIL import Image, ImageTk


# Initialize the main window
root = tk.Tk()
root.title("FOODIE LOGIN")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

# Function to switch between frames
def show_frame(frame):
    frame.tkraise()

# Function to open the main application page
def open_main_page():
    # Clear existing widgets from root
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Main Page")
    root.geometry('900x550')
    root.configure(bg='pink')

    # Load the image
    try:
        img = Image.open(r'D:\project python\bgbutton.png')
        img = ImageTk.PhotoImage(img)
    except Exception as e:
        messagebox.showerror("Image Error", f"Error loading image: {e}")
        return

    background_label = tk.Label(root, image=img)
    background_label.place(x=50, y=50)
    root.img = img  # Keep a reference to avoid garbage collection

    frame = tk.Frame(root, width=350, height=350, bg='pink')
    frame.place(x=480, y=70)

    # Buttons
    btn_food_calorie = tk.Button(frame, text="Food Calorie Count", font=("Helvetica", 16), width=25, height=3,
                                  activebackground="blue", activeforeground="black",
                                  command=open_food_calorie_finder, borderwidth=20, relief="sunken")
    btn_food_calorie.place(x=10, y=20)

    btn_diet_tracker = tk.Button(frame, text="Diet Tracker", font=("Helvetica", 16), width=25, height=3,
                                  activebackground="blue", activeforeground="black",
                                  command=open_add_calories, borderwidth=20, relief="sunken")
    btn_diet_tracker.place(x=10, y=120)

    btn_recipie_page = tk.Button(frame, text="Recipie Page", font=("Helvetica", 16), width=25, height=3,
                                  activebackground="blue", activeforeground="black",
                                  command=open_recipe_page, borderwidth=20, relief="sunken")
    btn_recipie_page.place(x=10, y=220)




# Function to handle registration
def handle_registration():
    try:
        username = reg_user.get()
        password = reg_code.get()
        email = reg_email.get()

        if username and password and email:
            # Check if the user already exists
            mycur.execute("SELECT * FROM reg_info WHERE username = %s", (username,))
            user = mycur.fetchone()

            if user:
                # If the user exists, log them in
                messagebox.showinfo("Login Success", "User already exists. Logging in...")
                show_frame(login_frame)
                user_entry.delete(0, END)
                user_entry.insert(0, username)
                password_entry.delete(0, END)
                password_entry.insert(0, password)
                # Open main page
                open_main_page()
                reg_frame.destroy()
            else:
                # If the user doesn't exist, register them
                mycur.execute("INSERT INTO reg_info (username, password, email) VALUES (%s, %s, %s);", (username, password, email))
                db_con.commit()
                messagebox.showinfo("Registration Success", "User registered successfully! Logging in...")
                show_frame(login_frame)
                user_entry.delete(0, END)
                user_entry.insert(0, username)
                password_entry.delete(0, END)
                password_entry.insert(0, password)
                # Open main page
                open_main_page()
              
                reg_frame.destroy()
        else:
            messagebox.showwarning("Input Error", "Please fill out all fields.")
    except IntegrityError:
        messagebox.showwarning("Duplicate Entry", "The username already exists. Please choose a different one.")
    except Exception as e:
        messagebox.showerror("Database Error", f"Error during database operation: {e}")

# Function to handle login
def handle_login():
    try:
        username = user_entry.get()
        password = password_entry.get()

        if username and password:
            # Check if the username and password match
            mycur.execute("SELECT * FROM reg_info WHERE username = %s AND password = %s", (username, password))
            user = mycur.fetchone()

            if user:
                messagebox.showinfo("Login Success", "You have successfully logged in.")
                # Open main page
                open_main_page()
                login_frame.destroy()
            else:
                messagebox.showerror("Login Failed", "Incorrect username or password.")
        else:
            messagebox.showwarning("Input Error", "Please enter both username and password.")
    except Exception as e:
        messagebox.showerror("Database Error", f"Error during database operation: {e}")

# Database connection (established once at the start)
try:
    db_con = connect(user='root', password='zineera', host='localhost', database='Regestration')
    mycur = db_con.cursor()
except Exception as e:
    messagebox.showerror("Database Error", f"Error connecting to the database: {e}")
    root.destroy()

# Login Frame
login_frame = Frame(root, width=925, height=500, bg="white")
login_frame.place(x=0, y=0)

# Registration Frame
reg_frame = Frame(root, width=925, height=500, bg="white")
reg_frame.place(x=0, y=0)

# Image for both frames
img = PhotoImage(file='reg.png')
Label(login_frame, image=img, bg="white").place(x=50, y=50)
Label(reg_frame, image=img, bg="white").place(x=50, y=50)

# Login Frame Design
login_panel = Frame(login_frame, width=350, height=350, bg="white")
login_panel.place(x=480, y=70)

heading = Label(login_panel, text='Sign In', fg='#57a1f8', bg='white', font=('Microsoft YaHie UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# Username Entry for Login
def on_enter_user(e):
    if user_entry.get() == 'username':
        user_entry.delete(0, 'end')

def on_leave_user(e):
    if user_entry.get() == '':
        user_entry.insert(0, 'username')

user_entry = Entry(login_panel, width=25, fg='black', bg='white', border=2, font=('Microsoft YaHie UI Light', 11, 'bold'))
user_entry.place(x=30, y=80)
user_entry.insert(0, 'username')
user_entry.bind('<FocusIn>', on_enter_user)
user_entry.bind('<FocusOut>', on_leave_user)

Frame(login_panel, width=295, height=2, bg='black').place(x=25, y=107)

# Password Entry for Login
def on_enter_password(e):
    if password_entry.get() == 'Enter your password':
        password_entry.delete(0, 'end')
        password_entry.config(show='*')

def on_leave_password(e):
    if password_entry.get() == '':
        password_entry.config(show='')
        password_entry.insert(0, 'Enter your password')

password_entry = Entry(login_panel, width=25, fg='black', bg='white', border=2, font=('Microsoft YaHie UI Light', 11, 'bold'))
password_entry.place(x=30, y=150)
password_entry.insert(0, 'Enter your password')
password_entry.bind('<FocusIn>', on_enter_password)
password_entry.bind('<FocusOut>', on_leave_password)

Frame(login_panel, width=295, height=2, bg='black').place(x=25, y=177)

# Sign In Button
Button(login_panel, width=39, pady=7, text='SIGN IN', bg='#57a1f8', fg='white', border=0, command=handle_login).place(x=35, y=204)

# Sign Up Label and Button
label = Label(login_panel, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHie UI Light', 9))
label.place(x=75, y=270)

sign_up_button = Button(login_panel, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=lambda: show_frame(reg_frame))
sign_up_button.place(x=215, y=270)

# Registration Frame Design
reg_panel = Frame(reg_frame, width=350, height=350, bg="white")
reg_panel.place(x=480, y=70)

heading = Label(reg_panel, text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft YaHie UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# Username Entry for Registration
def on_enter_reg_user(e):
    if reg_user.get() == 'username':
        reg_user.delete(0, 'end')

def on_leave_reg_user(e):
    if reg_user.get() == '':
        reg_user.insert(0, 'username')

reg_user = Entry(reg_panel, width=25, fg='black', bg='white', border=2, font=('Microsoft YaHie UI Light', 11, 'bold'))
reg_user.place(x=30, y=80)
reg_user.insert(0, 'username')
reg_user.bind('<FocusIn>', on_enter_reg_user)
reg_user.bind('<FocusOut>', on_leave_reg_user)

Frame(reg_panel, width=295, height=2, bg='black').place(x=25, y=107)

# Password Entry for Registration
def on_enter_reg_password(e):
    if reg_code.get() == 'Enter your password':
        reg_code.delete(0, 'end')
        reg_code.config(show='*')

def on_leave_reg_password(e):
    if reg_code.get() == '':
        reg_code.config(show='')
        reg_code.insert(0, 'Enter your password')

reg_code = Entry(reg_panel, width=25, fg='black', bg='white', border=2, font=('Microsoft YaHie UI Light', 11, 'bold'))
reg_code.place(x=30, y=150)
reg_code.insert(0, 'Enter your password')
reg_code.bind('<FocusIn>', on_enter_reg_password)
reg_code.bind('<FocusOut>', on_leave_reg_password)

Frame(reg_panel, width=295, height=2, bg='black').place(x=25, y=177)

# Email Entry for Registration
def on_enter_reg_email(e):
    if reg_email.get() == 'Enter your email':
        reg_email.delete(0, 'end')

def on_leave_reg_email(e):
    if reg_email.get() == '':
        reg_email.insert(0, 'Enter your email')

reg_email = Entry(reg_panel, width=25, fg='black', bg='white', border=2, font=('Microsoft YaHie UI Light', 11, 'bold'))
reg_email.place(x=30, y=205)
reg_email.insert(0, 'Enter your email')
reg_email.bind('<FocusIn>', on_enter_reg_email)
reg_email.bind('<FocusOut>', on_leave_reg_email)

Frame(reg_panel, width=295, height=2, bg='black').place(x=25, y=247)

# Sign Up Button with registration function
Button(reg_panel, width=39, pady=7, text='SIGN UP', bg='#57a1f8', fg='white', border=0, command=handle_registration).place(x=35, y=270)

# Back to Login Label and Button
label = Label(reg_panel, text="Already have an account?", fg='black', bg='white', font=('Microsoft YaHie UI Light', 9))
label.place(x=75, y=320)

login_button = Button(reg_panel, text='Sign In', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=lambda: show_frame(login_frame))
login_button.place(x=215, y=320)

# Show the login frame first
show_frame(login_frame)

root.mainloop()

# Close the database connection when the application is closed
db_con.close()
