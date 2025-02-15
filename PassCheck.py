from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Password Strength Checker")
root.configure(bg="#2c3e50")
root.iconbitmap(default="Checker.ico")

"""ENTRY"""
CheckEntry = ttk.Entry(root, font=("Arial", 12), width=30)
CheckEntry.grid(row=2, column=2, padx=10, pady=10)

"""DEF"""
def RatePass():
    global Rate
    Pass = CheckEntry.get()
    Rate = 0
    Digits = '1234567890'
    UpperLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LowerLetters = 'abcdefghijklmnopqrstuvwxyz'
    Symbols = '!@#$%^&*()-+[]{}:;"<>/\\|~'
    MinLen = 7
    if len(Pass) < MinLen:
        Rate += 5
    if any(char in Digits for char in Pass):
        Rate += 1
    if any(char in UpperLetters for char in Pass):
        Rate += 1
    if any(char in LowerLetters for char in Pass):
        Rate += 1
    if any(char in Symbols for char in Pass):
        Rate += 1

def CheckPass():
    RatePass()
    print("Password Strength:", Rate)
    if Rate == 5:
        PassLabel.config(text="❌ Password too short!", fg="#e74c3c")
    elif Rate == 0:
        PassLabel.config(text="", fg="#ecf0f1")
    elif Rate == 1:
        PassLabel.config(text="⚠️ Very Weak", fg="#e74c3c")
    elif Rate == 2:
        PassLabel.config(text="🔸 Weak", fg="#f39c12")
    elif Rate == 3:
        PassLabel.config(text="🔹 Average", fg="#f1c40f")
    elif Rate == 4:
        PassLabel.config(text="✅ Strong", fg="#2ecc71")

"""BUTTONS"""
CheckButton = ttk.Button(root, text="Check Password", command=CheckPass)
CheckButton.grid(row=3, column=2, padx=10, pady=10)

"""LABELS"""
CheckLabel = Label(root, text="Enter your password below:", font=("Arial", 12), bg="#2c3e50", fg="white")
CheckLabel.grid(row=1, column=2, padx=10, pady=10)

PassLabel = Label(root, text="", font=("Arial", 12, "bold"), bg="#2c3e50")
PassLabel.grid(row=4, column=2, padx=10, pady=10)

root.mainloop()
