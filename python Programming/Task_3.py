import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError("Length must be a positive integer.")

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        result_label.config(text=f"Generated Password: {password}")
        copy_button.config(state=tk.NORMAL)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for the length.")

def copy_password():
    password = result_label.cget("text").replace("Generated Password: ", "")
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")


length_label = tk.Label(root, text="Enter desired length of password:")
length_label.grid(row=0, column=0, padx=10, pady=10)


length_entry = tk.Entry(root, width=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)


generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)


result_label = tk.Label(root, text="Generated Password: ")
result_label.grid(row=2, column=0, columnspan=2, pady=10)


copy_button = tk.Button(root, text="Copy Password", command=copy_password, state=tk.DISABLED)
copy_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
