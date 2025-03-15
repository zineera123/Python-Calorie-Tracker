import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import pandas as pd
from con_reg import *
# Load data from CSV at the start
data_file_path = r"D:\project python\Food data.csv"
data = pd.read_csv(data_file_path, encoding="cp1252")

# Assuming the CSV has columns: 'Food Item' and 'Calories'
def get_calories(Food):
    global data
    # Find the row where 'Food Item' matches the input
    result = data[data['Food'].str.lower() == Food.lower()]
    if not result.empty:
        return result['Calories'].values[0]
    return None

healthy_recipes = {
    "Monday": {
        "Breakfast": "Oats with fruits and nuts",
        "Lunch": "Brown rice with moong dal and mixed vegetable sabzi",
        "Dinner": "Grilled fish with vegetables / paneer for (vegetarian)"
    },
    "Tuesday": {
        "Breakfast": "Vegetable smoothie(green vegies should be included) with chia seeds",
        "Lunch": "Palak salad with yoghurt and mixed greens veggies",
        "Dinner": "Whole wheat chapati with palak paneer and cucumber salad"
    },
    "Wednesday": {
        "Breakfast": "Whole wheat bread with boiled eggs",
        "Lunch": "Vegetable curry and brown rice",
        "Dinner": "Chicken/veg soup with a side of steamed veggies"
    },
    "Thursday": {
        "Breakfast": "Idli made with brown rice and sambar",
        "Lunch": "Barley khichdi with mixed vegetables and curd",
        "Dinner": "Grilled chicken breast with soup"
    },
    "Friday": {
        "Breakfast": "Smoothie bowl with banana/apple, nuts, and seeds",
        "Lunch": "Oats roti with spinach dal and a side of salad",
        "Dinner": "Paneer curry with brown rice"
    },
    "Saturday": {
        "Breakfast": "Ragi dosa with coconut chutney and sambar",
        "Lunch": "Chicken/paneer salad with roasted vegetables",
        "Dinner": "Grilled fish with sweet potato mash and a green salad"
    },
    "Sunday": {
        "Breakfast": "Greek yogurt and fresh fruits, protein powder",
        "Lunch": "Chicken and vegetable curry with brown rice",
        "Dinner": "Vegetable salad with a side of roasted cauliflower"
    },
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
    recipe_window = tk.Toplevel(root)
    recipe_window.title("Healthy Indian Diet Recipes")
    recipe_window.geometry("500x400")
    recipe_window.resizable(0, 0)
    recipe_window.configure(bg='pink')
    
    # Title Label
    title_label = tk.Label(recipe_window, text="Weekly Healthy Indian Diet Plan", font=("Helvetica", 18, "bold"), bg="white")
    title_label.place(x=60, y=20)

    # Day selection label
    day_label = tk.Label(recipe_window, text="Select a Day:", font=("Helvetica", 14), bg="white")
    day_label.place(x=50, y=80)

    # Day Combobox
    day_combobox = ttk.Combobox(recipe_window, values=list(healthy_recipes.keys()), font=("Helvetica", 12))
    day_combobox.place(x=180, y=80)

    # Show recipes button
    show_button = tk.Button(recipe_window, text="Show Recipes", font=("Helvetica", 10), width=10, height=1,
                             activebackground="blue", activeforeground="black",
                             borderwidth=10, relief="ridge", command=show_recipes)
    show_button.place(x=200, y=120)

    # Labels to display recipes
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

    recipe_window.mainloop()

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
    add_calories_window = tk.Toplevel(root, bg='light pink')
    add_calories_window.title("Calorie Counter")
    add_calories_window.geometry("500x350")
    add_calories_window.resizable(0, 0)
    
    total_calories = [0]

    # Place widgets using place()
    meal_label = tk.Label(add_calories_window, text="Meal:")
    meal_label.place(x=50, y=20)

    meal_entry = tk.Entry(add_calories_window)
    meal_entry.place(x=150, y=20)

    calories_label = tk.Label(add_calories_window, text="Calories:")
    calories_label.place(x=50, y=60)

    calories_entry = tk.Entry(add_calories_window)
    calories_entry.place(x=150, y=60)

    add_button = tk.Button(add_calories_window, text="Add", font=("Helvetica", 10), width=10, height=1,
                           activebackground="blue", activeforeground="black",
                           borderwidth=10, relief="sunken", command=add_calories)
    add_button.place(x=100, y=100)

    clear_button = tk.Button(add_calories_window, text="Clear List", command=clear_list)
    clear_button.place(x=250, y=100)

    calorie_list = tk.Listbox(add_calories_window, width=50)
    calorie_list.place(x=50, y=150)

    total_calories_label = tk.Label(add_calories_window, text="Total Calories: 0")
    total_calories_label.place(x=200, y=300)

def open_food_calorie_finder():
    food_calorie_finder_window()

def food_calorie_finder_window():
    calorie_finder = tk.Toplevel()  # Use Toplevel to create a new window
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

    calorie_finder.mainloop()

def open_main_page():
    global root
    root = tk.Tk()
    root.title("Main Page")
    root.geometry('900x550')
    root.resizable(0, 0)
    root.configure(bg='pink')

    img = tk.PhotoImage(file=r'bgbutton.png')  # Set your image file path
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

    root.mainloop()

# Call the function to setup and open the main page
open_main_page()
