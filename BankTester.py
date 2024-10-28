import tkinter as tk
from tkinter import messagebox

# Dictionary of allowed username-password pairs
allowed_credentials = {
    "user123": "password1",
    "user456": "password2",
    "user789": "password3",
    "user321": "password4",
    "user654": "password5"
}

# Function to handle login button click
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Check if username and password match any of the allowed credentials
    if username in allowed_credentials and allowed_credentials[username] == password:
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create main application window
root = tk.Tk()
root.title("Bank Terminal Login")
root.geometry("300x200")

# Username label and entry
username_label = tk.Label(root, text="Username")
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Password label and entry
password_label = tk.Label(root, text="Password")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")  
password_entry.pack(pady=5)

# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=10)

# Run the application
root.mainloop()
