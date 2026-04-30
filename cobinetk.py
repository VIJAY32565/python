import tkinter as tk

def login():
    user = entry_user.get()
    pwd = entry_pass.get()
    print("USERNAME:", user)
    print("PASSWORD:", pwd)

root = tk.Tk()
root.geometry("300x200")

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Login", command=login).pack()

root.mainloop()