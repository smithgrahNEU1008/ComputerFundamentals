import tkinter as tk
from tkinter import messagebox


allowed_credentials = {
    "user123": "password1",
    "user456": "password2",
    "user789": "password3",
    "user321": "password4",
    "user654": "password5"
}


account_balances = {
    "Checking": 1500.00,
    "Savings": 3000.00,
    "Credit Card": -500.00
}


def login():
    username = username_entry.get()
    password = password_entry.get()
    

    if username in allowed_credentials and allowed_credentials[username] == password:
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        show_balance_screen()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
        password_entry.delete(0, tk.END)  # Clear password field for security


def show_balance_screen():
    
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Account Balances")

    
    for account, balance in account_balances.items():
        account_button = tk.Button(root, text=f"{account}: ${balance:.2f}", font=("Arial", 12),
                                   command=lambda acc=account: show_account_details(acc))
        account_button.pack(pady=10)


def show_account_details(account):
    
    for widget in root.winfo_children():
        widget.destroy()

    root.title(f"{account} Details")

 
    account_label = tk.Label(root, text=f"{account} Account", font=("Arial", 14))
    account_label.pack(pady=10)

    balance_label = tk.Label(root, text=f"Balance: ${account_balances[account]:.2f}", font=("Arial", 12))
    balance_label.pack(pady=10)


    back_button = tk.Button(root, text="Back", command=show_balance_screen)
    back_button.pack(pady=10)


root = tk.Tk()
root.title("Bank Terminal Login")
root.geometry("300x200")


username_label = tk.Label(root, text="Username")
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)


password_label = tk.Label(root, text="Password")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")  # Hide password input
password_entry.pack(pady=5)


login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=10)

root.mainloop()
