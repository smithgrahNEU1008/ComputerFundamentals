import tkinter as tk
from tkinter import messagebox
import bcrypt
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch and hash plain text passwords from environment variables
hashed_credentials = {
    "user1": bcrypt.hashpw(os.getenv("USER1_PASSWORD").encode(), bcrypt.gensalt()) if os.getenv("USER1_PASSWORD") else None,
    "user4": bcrypt.hashpw(os.getenv("USER4_PASSWORD").encode(), bcrypt.gensalt()) if os.getenv("USER4_PASSWORD") else None,
    "user7": bcrypt.hashpw(os.getenv("USER7_PASSWORD").encode(), bcrypt.gensalt()) if os.getenv("USER7_PASSWORD") else None,
    "user3": bcrypt.hashpw(os.getenv("USER3_PASSWORD").encode(), bcrypt.gensalt()) if os.getenv("USER3_PASSWORD") else None,
    "user6": bcrypt.hashpw(os.getenv("USER6_PASSWORD").encode(), bcrypt.gensalt()) if os.getenv("USER6_PASSWORD") else None
}

# Print hashed credentials to verify they are loaded correctly
print("Loaded hashed credentials:", hashed_credentials)

account_balances = {
    "Checking": 1500.00,
    "Savings": 3000.00,
    "Credit Card": -500.00
}

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in hashed_credentials and hashed_credentials[username] is not None:
        if bcrypt.checkpw(password.encode(), hashed_credentials[username]):
            messagebox.showinfo("Login Success", f"Welcome, {username}!")
            show_balance_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
            password_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
        password_entry.delete(0, tk.END)

def show_balance_screen():
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Account Balances")

    for account, balance in account_balances.items():
        account_button = tk.Button(root, text=f"{account}: ${balance:.2f}", font=("Arial", 14),
                                   command=lambda acc=account: show_account_details(acc))
        account_button.pack(pady=10)

def show_account_details(account):
    for widget in root.winfo_children():
        widget.destroy()

    root.title(f"{account} Details")

    account_label = tk.Label(root, text=f"{account} Account", font=("Arial", 16))
    account_label.pack(pady=10)

    balance_label = tk.Label(root, text=f"Balance: ${account_balances[account]:.2f}", font=("Arial", 14))
    balance_label.pack(pady=10)

    back_button = tk.Button(root, text="Back", font=("Arial", 12), command=show_balance_screen)
    back_button.pack(pady=10)

root = tk.Tk()
root.title("Bank Terminal Login")
root.geometry("1600x900")

# Positioning elements in the top-right quarter of the screen
username_label = tk.Label(root, text="Username", font=("Arial", 18))
username_label.place(x=1100, y=50)

username_entry = tk.Entry(root, font=("Arial", 16), width=20)
username_entry.place(x=1250, y=50)

password_label = tk.Label(root, text="Password", font=("Arial", 18))
password_label.place(x=1100, y=100)

password_entry = tk.Entry(root, show="*", font=("Arial", 16), width=20)
password_entry.place(x=1250, y=100)

login_button = tk.Button(root, text="Login", font=("Arial", 16), width=10, height=2, command=login)
login_button.place(x=1300, y=160)

root.mainloop()
