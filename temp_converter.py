import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x350")
root.configure(bg="#a5e5ed")
title = tk.Label(root, text="🌡️Temperature Converter", font=("Segoe UI Emoji", 18,"bold"), bg="#e4eef0",fg="#2c3e50")
title.pack(pady=10)
input_label = tk.Label(root, text="Enter Temperature:", font=("Segoe UI", 11), bg="#3952e4", fg="#fff")
input_label.pack(pady=5)
entry = ttk.Entry(root, font=("Segoe UI", 13),justify="center")
entry.pack(pady=10)
unit_label = tk.Label(root, text="Select Unit:", font=("Segoe UI", 11), bg="#3952e4", fg="#fff")
unit_label.pack(pady=5)
unit_var = tk.StringVar(value="Celsius")
dropdown = tk.OptionMenu(root, unit_var,"Celsius","Fahrenheit","Kelvin")  
dropdown.config(font=("Segoe UI", 12), width=10, bg="#e7ebef", fg="#2c3e50")
dropdown.pack(pady=5)
result_heading=tk.Label(root, text="Converted Temperature:", font=("Segoe UI", 11), bg="#3952e4", fg="#fff" )
result_heading.pack()
result = tk.StringVar()
result_label=tk.Label(root, textvariable=result, font=("Helvetica", 13), bg="#f0f1f7", fg="#333")
result_label.pack(pady=10)

def convert():
    try:
        temp = float(entry.get())
        unit = unit_var.get()
        if unit == "Celsius":
            f=temp*9/5 + 32
            k=temp + 273.15
            result.set(f"{temp}°C={round(f,2)}°F = {round(k,2)}K❄️")
        elif unit == "Fahrenheit":
            c=(temp - 32) * 5/9
            k=c + 273.15
            result.set(f"{temp}°F={round(c,2)}°C = {round(k,2)}K")
        elif unit == "Kelvin":
            c=temp - 273.15
            f=c * 9/5 + 32
            result.set(f"{temp}K={round(c,2)}°C = {round(f,2)}°F")
    except ValueError:
        result.set("Invalid input. Please enter a number.")
convert_button = tk.Button(root,text="Convert", command=convert, font=("Segoe UI", 12,"bold"), bg="#4CAF50", fg="white", padx=10)
convert_button.pack(pady=5)
root.mainloop()
