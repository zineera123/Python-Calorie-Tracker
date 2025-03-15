# Python-Calorie-Tracker


# Healthy Diet Tracker and Calorie Finder

This is a Python-based application using `Tkinter` and `Pandas` to help users track their daily calorie intake, find the calorie content of food items, and access a weekly healthy diet plan with recipes.

## Features

- **Food Calorie Finder**: Allows the user to search for the calorie content of different food items from a CSV file.
- **Diet Tracker**: Users can add meals and their corresponding calorie content to track their total daily calorie intake.
- **Healthy Recipes**: Displays a weekly healthy Indian diet plan with recipes for each day of the week (Breakfast, Lunch, Dinner).

## Prerequisites

Make sure you have Python installed along with the required libraries:

- `Tkinter` for the graphical user interface (GUI).
- `Pandas` for handling the CSV data.
- `Pillow` for working with images.

To install the required libraries, you can use `pip`:

```bash
pip install pandas pillow
```

## Setup

1. **Download the project files**: Clone this repository to your local machine.

```bash
git clone https://github.com/yourusername/healthy-diet-tracker.git
```

2. **Prepare the data**: Ensure that the `Food data.csv` file is located in the correct directory. Update the path to this file in the script if necessary. It should contain food items and their corresponding calorie values.

3. **Image Files**: Ensure that the image files like `count.png` and `bgbutton.png` are in the correct directory or update the paths to match your local setup.

## Usage

To start the application, run the main Python script `diet_tracker.py`:

```bash
python diet_tracker.py
```

This will open the main window with the following options:
- **Food Calorie Count**: Find the calories for various food items.
- **Diet Tracker**: Add meals and track total daily calories.
- **Recipe Page**: View healthy Indian diet recipes for the week.

### Calorie Finder

- Enter a food item and click "Get Calories" to see the calorie content.
- If the food item is found in the CSV file, the calorie count will be displayed in a popup.

### Diet Tracker

- Add meals and their calorie content.
- The total calorie count for the day will be updated dynamically.
- You can clear the list to start fresh.

### Weekly Recipes

- Select a day from the dropdown and click "Show Recipes" to view healthy recipes for that day.

## Example CSV Format

The `Food data.csv` should be structured as follows:

```csv
Food,Calories
Apple,52
Banana,89
Rice,130
Chicken,165
```

## Screenshots

![Main Page](assets/main_page.png)

*Main application window showing the buttons for different features.*

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### How to use:
1. **Clone the repository** using the command:
   ```bash
   git clone https://github.com/yourusername/healthy-diet-tracker.git
   ```

2. **Install dependencies**:
   ```bash
   pip install pandas pillow
   ```

3. **Run the application**:
   ```bash
   python diet_tracker.py
   ```

You can now use the application to track calories, search for food calorie content, and view healthy diet recipes for each day of the week.

---

This `README.md` file is now ready for you to copy-paste directly into your GitHub repository. Be sure to replace placeholders like `https://github.com/yourusername/healthy-diet-tracker.git` with the actual URL of your GitHub repository.
