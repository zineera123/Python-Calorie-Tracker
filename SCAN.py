import tkinter as tk
from tkinter import messagebox
import cv2
from pyzbar.pyzbar import decode
import requests
from PIL import Image, ImageTk

# Function to fetch nutrition info using Nutritionix API
def get_nutrition_info(barcode):
    api_url = "https://api.nutritionix.com/v1_1/item"
    app_id = "YOUR_APP_ID"  # Replace with your Nutritionix App ID
    app_key = "YOUR_APP_KEY"  # Replace with your Nutritionix App Key
    response = requests.get(f"{api_url}/{barcode}", params={"appId": app_id, "appKey": app_key})
    
    if response.status_code == 200:
        data = response.json()
        if 'item_name' in data:
            food_name = data['item_name']
            calories = data['nf_calories']
            messagebox.showinfo("Food Nutrition", f"{food_name} contains {calories} kcal.")
        else:
            messagebox.showwarning("No Data", "No nutritional information found for this barcode.")
    else:
        messagebox.showerror("API Error", "Failed to fetch nutritional data. Please try again later.")

# Function to open the barcode scanner window
def open_barcode_scanner():
    scanner_window = tk.Toplevel()
    scanner_window.title("Barcode Scanner")
    scanner_window.geometry("800x600")
    scanner_window.resizable(0, 0)

    # Start capturing from the webcam
    cap = cv2.VideoCapture(0)
    
    # Canvas to display the webcam feed
    canvas = tk.Canvas(scanner_window, width=640, height=480)
    canvas.pack()
    
    def update_frame():
        ret, frame = cap.read()
        if ret:
            # Convert frame to RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_image = ImageTk.PhotoImage(image=Image.fromarray(frame_rgb))
            
            # Display the frame on the canvas
            canvas.create_image(0, 0, anchor="nw", image=frame_image)
            canvas.image = frame_image  # Keep reference to avoid garbage collection

            # Decode barcodes in the frame
            barcodes = decode(frame)
            for barcode in barcodes:
                barcode_data = barcode.data.decode("utf-8")
                get_nutrition_info(barcode_data)  # Fetch nutritional info using barcode
                
                # Stop the video capture after scanning a barcode
                cap.release()
                scanner_window.destroy()
                break

        # Update the frame every 10 milliseconds
        scanner_window.after(10, update_frame)

    # Start the frame updates
    update_frame()

