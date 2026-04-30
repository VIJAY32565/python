import tkinter as tk

def click():
    print("rideo button")

root = tk.Tk()
root.geometry("")

# Corrected: Button with capital B
button = tk.Button(root, text="click me", command=click)
button.pack()

root.mainloop()
