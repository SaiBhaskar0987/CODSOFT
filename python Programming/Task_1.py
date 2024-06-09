import tkinter as tk
from tkinter import messagebox

def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

def clear_placeholder(event):
    if entry.get() == "Add task here":
        entry.delete(0, tk.END)
        entry.config(fg='black')

def add_placeholder(event):
    if entry.get() == "":
        entry.insert(0, "Add task here")
        entry.config(fg='grey')

def add_task():
    task_text = entry.get()
    if task_text != "" and task_text != "Add task here":
        task_var = tk.BooleanVar()
        task = tk.Checkbutton(task_frame, text=task_text, variable=task_var)
        task.pack(anchor='w')
        tasks.append(task)
        task_vars.append(task_var)
        entry.delete(0, tk.END)
        add_placeholder(None)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    for i in range(len(tasks) - 1, -1, -1):
        if task_vars[i].get():
            tasks[i].destroy()
            del tasks[i]
            del task_vars[i]

root = tk.Tk()
root.title("To-Do List Application")


frame = tk.Frame(root)
frame.pack(pady=10)

tasks = []
task_vars = []


canvas = tk.Canvas(frame, width=400, height=200)
canvas.pack(side=tk.LEFT, fill=tk.BOTH)


scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', on_canvas_configure)

task_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=task_frame, anchor="nw")


entry = tk.Entry(root, width=50)
entry.pack(pady=10)
entry.insert(0, "Add task here")
entry.bind("<FocusIn>", clear_placeholder)
entry.bind("<FocusOut>", add_placeholder)

add_button = tk.Button(root, text="Add Task", width=48, command=add_task, bd=2, highlightbackground='black')
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Selected Tasks", width=48, command=delete_task, bd=2, highlightbackground='black')
delete_button.pack(pady=5)

root.mainloop()
