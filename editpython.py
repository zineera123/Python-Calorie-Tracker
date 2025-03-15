import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import pandas as pd
from random import choice
import cv2
from pyzbar.pyzbar import decode
from con_reg import *


# Load data from CSV
data_file_path = r"D:\project python\Food data.csv"
data = pd.read_csv(data_file_path, encoding="cp1252")

# Assuming the CSV has columns: 'Food Item' and 'Calories'
def get_calories(Food):
    global data
    result = data[data['Food'].str.lower() == Food.lower()]
    if not result.empty:
        return result['Calories'].values[0]
    return None

# Barcode Scanner Function
def scan_barcode():
    cap = cv2.VideoCapture(0)  # Open the default camera
    if not cap.isOpened():
        messagebox.showerror("Camera Error", "Unable to access the camera.")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Decode the barcode in the image
        barcodes = decode(frame)
        for barcode in barcodes:
            barcode_data = barcode.data.decode("utf-8")
            barcode_type = barcode.type
            # Display barcode info on screen
            messagebox.showinfo("Barcode Data", f"Data: {barcode_data}\nType: {barcode_type}")

            # Search for the barcode data in your food dataset
            calories = get_calories(barcode_data)
            if calories is not None:
                messagebox.showinfo("Calories Information", f"{barcode_data} contains {calories} kcal.")
            else:
                messagebox.showwarning("No Data", "No calorie data found for this item")
            break  # We only need the first barcode found

        # Show the frame with barcode detected
        cv2.imshow("Barcode Scanner", frame)

        # Exit the scanner if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Sample dictionary for healthy recipes (modify as needed)
healthy_recipes = {
    "Monday": {
        "Breakfast": "Oats with milk and fruits",
        "Lunch": "Dal, roti, and vegetable curry",
        "Dinner": "Khichdi with curd"
    },
    "Tuesday": {
        "Breakfast": "Poha with peanuts and tea",
        "Lunch": "Rice, sambar, and a side of stir-fried vegetables",
        "Dinner": "Grilled chicken salad"
    },
    "Wednesday": {
        "Breakfast": "Idli with coconut chutney",
        "Lunch": "Rajma chawal",
        "Dinner": "Stuffed paratha with pickle and curd"
    },
    "Thursday": {
        "Breakfast": "Sprouts chaat and green tea",
        "Lunch": "Paneer bhurji with roti",
        "Dinner": "Vegetable soup with multigrain bread"
    },
    "Friday": {
        "Breakfast": "Upma with coconut chutney",
        "Lunch": "Fish curry with rice",
        "Dinner": "Grilled tofu with a side salad"
    },
    "Saturday": {
        "Breakfast": "Aloo paratha with curd",
        "Lunch": "Chicken biryani",
        "Dinner": "Methi thepla with pickle"
    },
    "Sunday": {
        "Breakfast": "Dosa with sambar",
        "Lunch": "Butter chicken with naan",
        "Dinner": "Light vegetable pulao"
    }
}

# Health tips list
health_tips = [
    "Stay hydrated! Drink at least 8 glasses of water a day.",
    "Eat a balanced diet with plenty of fruits and vegetables.",
    "Get at least 30 minutes of exercise every day.",
    "Include protein in every meal for muscle repair and growth.",
    "Limit sugar intake to maintain healthy blood sugar levels.",
    "Sleep 7-9 hours every night for optimal health.",
    "Take breaks during work to stretch and move around.",
    "Eat smaller meals more frequently to improve metabolism."
]

def show_health_tip():
    tip = choice(health_tips)  # Randomly select a health tip
    messagebox.showinfo("Health Tip", tip)

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

    day_combobox = ttk.Combobox(recipe_window, values=list(healthy_recipes.keys()), font=("Helvetica", 12), state="readonly")
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

# Placeholder for Food Calorie Finder function
def open_food_calorie_finder():
    messagebox.showinfo("Food Calorie Finder", "This feature will allow you to find food calories.")

# Placeholder for Add Calories function
def open_add_calories():
    messagebox.showinfo("Diet Tracker", "This feature will allow you to add calories for your diet.")

# Add the rest of your existing code as it is...

# Integrate the barcode scanner into your existing GUI
def open_barcode_scanner():
    scan_barcode()

# Main window with Barcode Scanner Button
def open_main_page():
    global root
    root = tk.Tk()
    root.title("Main Page")
    root.geometry('900x550')
    root.resizable(0, 0)
    root.configure(bg='pink')

    try:
        img = tk.PhotoImage(file=r'bgbutton.png')
        background_label = tk.Label(root, image=img)
        background_label.place(x=50, y=50)
        root.img = img  # Keep reference to avoid garbage collection
    except tk.TclError:
        messagebox.showerror("Image Error", "Could not load image 'bgbutton.png'. Please check the file path.")

    frame = tk.Frame(root, width=350, height=350, bg='pink')
    frame.place(x=480, y=70)

    btn_food_calorie = tk.Button(frame, text="Food Calorie Count", command=open_food_calorie_finder, borderwidth=20, relief="sunken")
    btn_food_calorie.place(x=10, y=120)

    btn_health_tip = tk.Button(frame, text="Health Tips", command=show_health_tip, borderwidth=20, relief="sunken")
    btn_health_tip.place(x=10, y=170)

    btn_recipie_page = tk.Button(frame, text="Healthy Recipes", command=open_recipe_page, borderwidth=20, relief="sunken")
    btn_recipie_page.place(x=10, y=220)

    btn_scanner = tk.Button(frame, text="Barcode Scanner", command=open_barcode_scanner, borderwidth=20, relief="sunken")
    btn_scanner.place(x=10, y=320)

    root.mainloop()

open_main_page()
