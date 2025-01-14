import tkinter as tk
from tkinter import messagebox

def sum():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 + num2
    messagebox.showinfo("Result", result)
    
def subtract():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 - num2
    messagebox.showinfo("Result", result)
    
def multiply():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 * num2
    messagebox.showinfo("Result", result)
    
def divide():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    if num2 == 0:
        messagebox.showerror("Error", "Cannot divide by zero your enty number")
    else:
        result = num1 / num2
        messagebox.showinfo("Result", result)

# Create window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("500x300") 
root.resizable(False, False) 
root.configure(bg="light blue")
root.configure(cursor="hand2")
root.configure(borderwidth=10)
root.configure(relief="flat") 
root.configure(highlightcolor="black") 
root.configure(highlightthickness=5)
root.configure(takefocus=True)
root.configure(width=500)
root.configure(height=300)
root.configure(cursor="arrow")





# Entry fields
entry1 = tk.Entry(root)
entry1.pack()
entry1.configure(bg="light yellow")
entry1.configure(fg="black")
entry1.configure(font="bold")
entry1.configure(width=20)

entry2 = tk.Entry(root)
entry2.pack()
entry2.configure(bg="light yellow")
entry2.configure(fg="black")
entry2.configure(font="bold")
entry2.configure(width=20)

# Buttons
button_sum = tk.Button(root, text="Add", command=sum)
button_sum.pack()
button_sum.configure(bg="light green")
button_sum.configure(fg="black") 
button_sum.configure(font="bold") 
button_sum.configure(width=20)
button_sum.configure(height=2)

button_subtract = tk.Button(root, text="Subtract", command=subtract)
button_subtract.pack()
button_subtract.configure(bg="light green")
button_subtract.configure(fg="black")
button_subtract.configure(font="bold")
button_subtract.configure(width=20)
button_subtract.configure(height=2)

button_multiply = tk.Button(root, text="Multiply", command=multiply)
button_multiply.pack()
button_multiply.configure(bg="light green")
button_multiply.configure(fg="black")
button_multiply.configure(font="bold")
button_multiply.configure(width=20)
button_multiply.configure(height=2)

button_divide = tk.Button(root, text="Divide", command=divide)
button_divide.pack()
button_divide.configure(bg="light green")
button_divide.configure(fg="black")
button_divide.configure(font="bold")
button_divide.configure(width=20)
button_divide.configure(height=2)

# Window loop
root.mainloop()