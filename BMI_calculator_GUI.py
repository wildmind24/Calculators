import tkinter as tk
from tkinter import messagebox

# To calculate BMI define a function
# Using try except, so incase user inputs are invalid
def calculate_bmi():
    try:
        # Getting the values from the user input(different because we are using GUI (tkinter) and not CLI)
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        # BMI formula: weight (kg) / (height (m))^2
        bmi = weight / (height ** 2)
        
        # Displaying the result of bmi
        bmi_result_label.config(text=f"BMI: {bmi:.2f}")
        
        # Categorizing BMI 
        if bmi < 18.5:
            category_label.config(text="Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            category_label.config(text="Category: Normal weight")
        elif 25 <= bmi < 29.9:
            category_label.config(text="Category: Overweight")
        else:
            category_label.config(text="Category: Obese")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Setting up the main window which shows
root = tk.Tk()
root.title("BMI Calculator")



# Creating labels and entry fields
weight_label = tk.Label(root, text="Enter your weight (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=20)

weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=20)

height_label = tk.Label(root, text="Enter your height (m):")
height_label.grid(row=1, column=0, padx=10, pady=20)

height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=20)


#Creating the button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=40)

# Label for displaying BMI result
bmi_result_label = tk.Label(root, text="BMI: N/A", font=("Arial", 14))
bmi_result_label.grid(row=3, column=0, columnspan=2)

# Label for displaying BMI category
category_label = tk.Label(root, text="Category: N/A", font=("Arial", 14))
category_label.grid(row=4, column=0, columnspan=2)

# Start the main loop to run the GUI
root.mainloop()