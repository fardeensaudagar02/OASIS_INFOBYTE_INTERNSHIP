import tkinter as tk
from tkinter import messagebox

class BMI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BMI Calculator")
        self.label = tk.Label(self.root, text="BMI Calculator")
        self.label.pack()
        self.label_age = tk.Label(self.root, text="Age:")
        self.label_age.pack()
        self.entry_age = tk.Entry(self.root)
        self.entry_age.pack()
        self.label_height = tk.Label(self.root, text="Height (cm):")
        self.label_height.pack()
        self.entry_height = tk.Entry(self.root)
        self.entry_height.pack()
        self.label_weight = tk.Label(self.root, text="Weight (kg):")
        self.label_weight.pack()
        self.entry_weight = tk.Entry(self.root)
        self.entry_weight.pack()
        self.button = tk.Button(self.root, text="Calculate", command=self.calculate_bmi)
        self.button.pack()
        
    def calculate_bmi(self):
        try:
            age = int(self.entry_age.get())
            height = int(self.entry_height.get())
            weight = int(self.entry_weight.get())
            if height == 0:
                messagebox.showerror("Error", "Height cannot be zero.")
                return
            height_in_meters = height / 100
            bmi = weight / (height_in_meters ** 2)
            if bmi <= 16:
                messagebox.showinfo("BMI Category", "Severe Thinness")
            elif 16 < bmi <= 17:
                messagebox.showinfo("BMI Category", "Mild Thinness")
            elif 17 < bmi <= 18.5:
                messagebox.showinfo("BMI Category", "Moderate Thinness")
            elif 18.5 < bmi <= 25:
                messagebox.showinfo("BMI Category", "Normal")
            elif 25 < bmi <= 30:
                messagebox.showinfo("BMI Category", "Overweight")
            elif 30 <= bmi <= 35:
                messagebox.showinfo("BMI Category", "Obese Class I")
            elif 35 <= bmi <= 40:
                messagebox.showinfo("BMI Category", "Obese Class II")
            elif bmi > 40:
                messagebox.showinfo("BMI Category", "Obese Class III")
        except ValueError:
            messagebox.showerror("Error", "Please enter numeric values for age, height, and weight.")
    def run(self):
        self.root.mainloop()
        
game = BMI()
game.run()
