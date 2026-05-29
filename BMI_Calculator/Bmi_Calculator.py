from tkinter import *
from tkinter import messagebox

def bmi():
    try:
        user = name.get()

        w = float(weight.get())
        h = float(height.get())/100

        b = round(w / (h * h), 2)

        if b < 18.5:
            msg = f"hey {user}, your BMI is {b}.\nYou are underweight.\nTry eating Banana, Milk and Eggs 🍌🥛"

        elif b < 25:
            msg = f"hey {user}, your BMI is {b}.\nYou are in a healthy range.\nMaintain your healthy food habits 🥗"

        elif b < 30:
            msg = f"hey {user}, your BMI is {b}.\nYou are slightly overweight.\nTry eating Oats, Salads and Green Tea 🥗"

        else:
            msg = f"hey {user}, your BMI is {b}.\nYou are in the obese category.\nAvoid junk food and eat Fruits & Vegetables 🍎"

        result.config(text=msg)

    except:
        messagebox.showerror("Error", "Please enter valid values")

root = Tk()

root.title("BMI Calculator")
root.geometry("500x450")
root.config(bg="lightblue")

Label(root,
text="BMI Calculator",
font=("Arial", 50, "bold"),
bg="lightblue").pack(pady=10)

# Name
Label(root,
text="Enter Your Name",
bg="lightblue",
font=("Arial", 15)).pack()

name = Entry(root)
name.pack(pady=5)

# Weight
Label(root,
text="Weight (kg)",
bg="lightblue",
font=("Arial", 15)).pack()

weight = Entry(root)
weight.pack(pady=5)

# Height
Label(root,
text="Height (cm)",
bg="lightblue",
font=("Arial", 15)).pack()

height = Entry(root)
height.pack(pady=5)

# Button
Button(root,
text="Calculate BMI",
command=bmi,
bg="blue",
fg="white",
font=("Arial", 15, "bold")).pack(pady=15)

# Result
result = Label(root,
text="",
font=("Arial", 30, "bold"),
bg="lightblue",
wraplength=380,
justify="center")

result.pack(pady=20)

root.mainloop()