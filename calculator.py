from tkinter import *

# Create the main window
root = Tk()
root.title("Simple Calculator")
root.geometry("320x480")
root.resizable(False, False)

# Entry field for display
entry = Entry(root, width=15, font=('Arial', 24), borderwidth=5, relief=RIDGE, justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)

# Function to handle button clicks
def click(val):
    entry.insert(END, val)

# Function to clear the entry field
def clear():
    entry.delete(0, END)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Define all buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Create and place all buttons dynamically
for (text, row, col) in buttons:
    if text == '=':
        btn = Button(root, text=text, padx=20, pady=20, font=('Arial', 18), bg='#ffa500',
                     command=evaluate)
    else:
        btn = Button(root, text=text, padx=20, pady=20, font=('Arial', 18),
                     command=lambda t=text: click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button (C)
clear_btn = Button(root, text='C', padx=80, pady=20, font=('Arial', 18), bg='#ff4444', fg='white',
                   command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, pady=10)

# Run the app
root.mainloop()
