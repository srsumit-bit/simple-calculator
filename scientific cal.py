import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Scientific Calculator")
        self.root.geometry("500x700")  # Adjust the window size
        self.expression = ""
        self.memory = 0
        self.is_radians = True  # Default to radians

        self.input_text = tk.StringVar()

        # Create input frame
        self.input_frame = tk.Frame(root, bd=5, relief=tk.RIDGE)
        self.input_frame.pack(side=tk.TOP)

        # Create input field
        self.input_field = tk.Entry(self.input_frame, font=('Arial', 20), textvariable=self.input_text, width=30, bd=5, insertwidth=4, relief=tk.RIDGE, justify='right')
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)

        # Create button frame
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        # Create all buttons
        self.create_buttons()

    def add_to_expression(self, value):
        # Handle function translations and parentheses
        if value == "π":
            value = str(math.pi)
        elif value == "e":
            value = str(math.e)
        elif value == "^":
            value = "**"
        elif value == "±":
            if self.expression and self.expression[0] == "-":
                self.expression = self.expression[1:]
            else:
                self.expression = "-" + self.expression
            self.input_text.set(self.expression)
            return
        elif value == "√":
            value = "math.sqrt("
        elif value == "log":
            value = "math.log10("
        elif value == "ln":
            value = "math.log("
        elif value == "sin":
            value = "math.sin(math.radians("
            if not self.is_radians:
                value = "math.sin("
        elif value == "cos":
            value = "math.cos(math.radians("
            if not self.is_radians:
                value = "math.cos("
        elif value == "tan":
            value = "math.tan(math.radians("
            if not self.is_radians:
                value = "math.tan("
        elif value == "!":
            try:
                self.expression = str(math.factorial(int(eval(self.expression))))
                self.input_text.set(self.expression)
            except:
                self.input_text.set("Error")
            return
        elif value == "M+":
            try:
                self.memory += float(self.expression)
                self.expression = ""
                self.input_text.set(self.memory)
            except:
                self.input_text.set("Error")
            return
        elif value == "M-":
            try:
                self.memory -= float(self.expression)
                self.expression = ""
                self.input_text.set(self.memory)
            except:
                self.input_text.set("Error")
            return
        elif value == "MC":
            self.memory = 0
            self.expression = ""
            self.input_text.set(self.memory)
            return
        elif value == "MR":
            self.expression = str(self.memory)
            self.input_text.set(self.expression)
            return
        elif value == "(":
            value = "("
        elif value == ")":
            value = ")"
        
        # Append the value to the expression
        self.expression += value
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except:
            self.input_text.set("Error")
            self.expression = ""

    def toggle_angle_mode(self):
        self.is_radians = not self.is_radians
        if self.is_radians:
            self.angle_mode_button.config(text="Rad")
        else:
            self.angle_mode_button.config(text="Deg")

    def create_buttons(self):
        # Define button layout with memory and angle mode toggle
        buttons = [
            ['C', '(', ')', '%', 'MC', 'MR'],
            ['7', '8', '9', '/', 'M+', 'M-'],
            ['4', '5', '6', '*', 'log', 'ln'],
            ['1', '2', '3', '-', 'sin', 'cos'],
            ['0', '.', '=', '+', 'tan', '±'],
            ['π', 'e', '^', '√', '!', 'Rad']
        ]

        # Create the buttons dynamically in a grid
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                button = tk.Button(self.button_frame, text=text, width=8, height=2, font=('Arial', 14), bd=2, relief=tk.RIDGE)
                button.grid(row=i, column=j, padx=2, pady=2)
                if text == "=":
                    button.config(command=self.evaluate)
                elif text == "C":
                    button.config(command=self.clear)
                elif text == "Rad" or text == "Deg":
                    button.config(command=self.toggle_angle_mode)
                else:
                    button.config(command=lambda val=text: self.add_to_expression(val))

# Run the enhanced calculator
root = tk.Tk()
calc = Calculator(root)
root.mainloop()
