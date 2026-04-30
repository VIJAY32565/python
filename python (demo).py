import tkinter as tk

# Functions to add numbers
def add_numbers():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 + num2
    result_label.config(text= "Result:"+ str(result))

# create window
root = tk.Tk()
root.title("Addition using Labels")
root.geometry("300x200")

#labels and entry boxes
label1 = tk.Label(root, text="Enter first number:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root,text="Enter second number:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

# Button
add_button = tk.Button(root, text="Add", command= add_numbers)
add_button.pack()

# Results label
result_label = tk.Label(root , text= "Result:")
result_label.pack()

# run the gui
root.mainloop()
