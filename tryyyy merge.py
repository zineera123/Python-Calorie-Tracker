# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:52:18 2024

@author: zineera kazi
"""

import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from pymysql import connect, IntegrityError
from PIL import Image, ImageTk
import pandas as pd

# Load data from CSV at the start
data_file_path = r"D:\project python\Food data.csv"
data = pd.read_csv(data_file_path, encoding="cp1252")

# Assuming the CSV has columns: 'Food Item' and 'Calories'
def get_calories(Food):
    global data
    result = data[data['Food'].str.lower() == Food.lower()]
    if not result.empty:
        return result['Calories'].values[0]
    return None

healthy_recipes = {
    # Your recipe data here...
}

def show_recipes():
    selected_day = day_combobox.get()
    if selected_day in healthy_recipes:
        breakfast_recipe.set(healthy_recipes[selected_day]['Breakfast'])
        lunch_recipe.set(healthy_recipes[selected_day]['Lunch'])
        dinner_recipe.set(healthy_recipes[selected_day]['Dinner'])
    else:
        messagebox.showerror("Selection Error", "Please select a valid day.")

def open_recipe_page():
    global day_combobox, breakfast_recipe, lunch_recipe, dinner_recipe
    root.withdraw()  # Hide the main window

    recipe_window = tk.Toplevel(root)
    recipe_window.title("Healthy Indian Diet Recipes")
    recipe_window.geometry("500x400")
    recipe_window.resizable(0, 0)
    recipe_window.configure(bg='pink')

    title_label = tk.Label(recipe_window, text="Weekly Healthy Indian Diet Plan", font=("Helvetica", 18, "bold"), bg="white")
    title_label.place(x=60, y=20)

    day_label = tk.Label(recipe_window, text="Select a Day:", font=("Helvetica", 14), bg="white")
    day_label.place(x=50, y=80)

    day_combobox = ttk.Combobox(recipe_window, values=list(healthy_recipes.keys()), font=("Helvetica", 12))
    day_combobox.place(x=180, y=80)

    show_button = tk.Button(recipe_window, text="Show Recipes", font=("Helvetica", 10), width=10, height=1,
                            activebackground="blue", activeforeground="black", borderwidth=10, relief="ridge", command=show_recipes)
    show_button.place(x=200, y=120)

    breakfast_label = tk.Label(recipe_window, text="Breakfast:", font=("Helvetica", 14), bg="white")
    breakfast_label.place(x=50, y=180)
    breakfast_recipe = tk.StringVar()
    breakfast_value = tk.Label(recipe_window, textvariable=breakfast_recipe, font=("Helvetica", 12), bg="white", wraplength=300)
    breakfast_value.place(x=150, y=180)

    lunch_label = tk.Label(recipe_window, text="Lunch:", font=("Helvetica", 14), bg="white")
    lunch_label.place(x=50, y=230)
    lunch_recipe = tk.StringVar()
    lunch_value = tk.Label(recipe_window, textvariable=lunch_recipe, font=("Helvetica", 12), bg="white", wraplength=300)
    lunch_value.place(x=150, y=230)

    dinner_label = tk.Label(recipe_window, text="Dinner:", font=("Helvetica", 14), bg="white")
    dinner_label.place(x=50, y=280)
    dinner_recipe = tk.StringVar()
    dinner_value = tk.Label(recipe_window, textvariable=dinner_recipe, font=("Helvetica", 12), bg="white", wraplength=300)
    dinner_value.place(x=150, y=280)

    # Handle closing the recipe window
    recipe_window.protocol("WM_DELETE_WINDOW", lambda: close_window(recipe_window))

def add_calories():
    global total_calories
    try:
        meal = meal_entry.get()
        calories = int(calories_entry.get())
        calorie_list.insert(tk.END, f"{meal}: {calories} calories")
        total_calories[0] += calories
        update_total_calories()
        meal_entry.delete(0, tk.END)
        calories_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for calories.")

def update_total_calories():
    total_calories_label.config(text=f"Total Calories: {total_calories[0]}")

def clear_list():
    global total_calories
    calorie_list.delete(0, tk.END)
    total_calories[0] = 0
    update_total_calories()

def open_add_calories():
    global meal_entry, calories_entry, calorie_list, total_calories_label, total_calories
    root.withdraw()  # Hide the main window

    add_calories_window = tk.Toplevel(root, bg='light pink')
    add_calories_window.title("Calorie Counter")
    add_calories_window.geometry("500x350")
    add_calories_window.resizable(0, 0)

    total_calories = [0]

    meal_label = tk.Label(add_calories_window, text="Meal:")
    meal_label.place(x=50, y=20)

    meal_entry = tk.Entry(add_calories_window)
    meal_entry.place(x=150, y=20)

    calories_label = tk.Label(add_calories_window, text="Calories:")
    calories_label.place(x=50, y=60)

    calories_entry = tk.Entry(add_calories_window)
    calories_entry.place(x=150, y=60)

    add_button = tk.Button(add_calories_window, text="Add", command=add_calories, borderwidth=10, relief="sunken")
    add_button.place(x=100, y=100)

    clear_button = tk.Button(add_calories_window, text="Clear List", command=clear_list)
    clear_button.place(x=250, y=100)

    calorie_list = tk.Listbox(add_calories_window, width=50)
    calorie_list.place(x=50, y=150)

    total_calories_label = tk.Label(add_calories_window, text="Total Calories: 0")
    total_calories_label.place(x=200, y=300)

    # Handle closing the calorie counter window
    add_calories_window.protocol("WM_DELETE_WINDOW", lambda: close_window(add_calories_window))

def open_food_calorie_finder():
    root.withdraw()  # Hide the main window

    calorie_finder = tk.Toplevel(root)
    calorie_finder.title("Food Calorie Finder")
    calorie_finder.geometry("500x500")
    calorie_finder.resizable(0, 0)
    calorie_finder.configure(bg='white')

    img = tk.PhotoImage(file=r'count.png')
    tk.Label(calorie_finder, image=img, bg='light blue').place(x=50, y=50)
    calorie_finder.img = img  # Keep a reference to avoid garbage collection

    def show_calories():
        food_item = food_entry.get()
        if not food_item:
            messagebox.showwarning("Input Error", "Please enter a food item")
            return
        calories = get_calories(food_item)
        if calories is not None:
            messagebox.showinfo("Calories Information", f"{food_item.title()} contains {calories} kcal.")
        else:
            messagebox.showwarning("No data", "No calorie data found for this item")
    
    label_food = tk.Label(calorie_finder, text="Enter food item", fg='black', bg='red', font=('Arial', 20, 'bold'))
    label_food.place(x=160, y=170)

    food_entry = tk.Entry(calorie_finder, width=30)
    food_entry.place(x=180, y=240)

    button_food = tk.Button(calorie_finder, text='Get Calories', command=show_calories, font=("Helvetica", 16))
    button_food.place(x=190, y=290)

    # Handle closing the calorie finder window
    calorie_finder.protocol("WM_DELETE_WINDOW", lambda: close_window(calorie_finder))

def close_window(window):
    window.destroy()
    root.deiconify()  # Show the main window again

# Database connection (established once at the start)
try:
    db_con = connect(user='root', password='zineera', host='localhost', database='Regestration')
    mycur = db_con.cursor()
except Exception as e:
    messagebox.showerror("Database Error", f"Error connecting to the database: {e}")
    root.destroy()

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
    root.withdraw()  # Hide the login window

    main_window = tk.Toplevel(root)
    main_window.geometry("925x500+300+200")
    main_window.configure(bg="light blue")
    
    tk.Label(main_window, text='Main Menu', font=('Arial', 30), bg='white').pack(pady=30)
    
    food_finder_btn = tk.Button(main_window, text="Food Calorie Finder", command=open_food_calorie_finder)
    food_finder_btn.pack(pady=20)
    
    add_calories_btn = tk.Button(main_window, text="Calorie Counter", command=open_add_calories)
    add_calories_btn.pack(pady=20)
    
    recipe_page_btn = tk.Button(main_window, text="Diet and Recipe Page", command=open_recipe_page)
    recipe_page_btn.pack(pady=20)
    
    main_window.protocol("WM_DELETE_WINDOW", lambda: close_window(main_window))

# Registration/Login logic goes here (As provided)
# Main application logic continues ...

root.mainloop()
