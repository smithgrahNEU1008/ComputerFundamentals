import tkinter as tk
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

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Clear previous error message
    error_label.config(text="")

    if username in hashed_credentials and hashed_credentials[username] is not None:
        if bcrypt.checkpw(password.encode(), hashed_credentials[username]):
            error_label.config(fg="white", text=f"Welcome, {username}!")
        else:
            error_label.config(fg="white", text="Login Failed: Invalid username or password.")
            password_entry.delete(0, tk.END)
    else:
        error_label.config(fg="white", text="Login Failed: Invalid username or password.")
        password_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Bank Terminal Login")
root.geometry("1024x768")
root.configure(bg="#f7f7f7")

# Create the top header bar
header_frame = tk.Frame(root, bg="#0047ab", height=50)
header_frame.pack(fill=tk.X, side=tk.TOP)

# Add a bank logo placeholder
logo_label = tk.Label(header_frame, text="BANK OF PYTHON", font=("Arial", 16, "bold"), bg="#0047ab", fg="white")
logo_label.pack(side=tk.LEFT, padx=10)

# Add navigation links
nav_links = ["Checking", "Savings & CDs", "Credit Cards", "Home Loans", "Auto Loans", "Investing", "Security"]
for link in nav_links:
    nav_button = tk.Button(header_frame, text=link, font=("Arial", 12), bg="#0047ab", fg="white", borderwidth=0)
    nav_button.pack(side=tk.LEFT, padx=10)

# Top Left: Login Box
login_frame = tk.Frame(root, bg="#d71a1a", width=400, height=250, relief="solid", borderwidth=1)
login_frame.place(x=20, y=70)

login_label = tk.Label(login_frame, text="Login to Your Account", font=("Arial", 18), bg="#d71a1a", fg="white")
login_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

error_label = tk.Label(login_frame, text="", font=("Arial", 12), bg="#d71a1a", fg="white")
error_label.place(x=30, y=60)

username_label = tk.Label(login_frame, text="Username", font=("Arial", 14), bg="#d71a1a", fg="white")
username_label.place(x=30, y=80)
username_entry = tk.Entry(login_frame, font=("Arial", 14), width=20)
username_entry.place(x=150, y=80)

password_label = tk.Label(login_frame, text="Password", font=("Arial", 14), bg="#d71a1a", fg="white")
password_label.place(x=30, y=130)
password_entry = tk.Entry(login_frame, show="*", font=("Arial", 14), width=20)
password_entry.place(x=150, y=130)

login_button = tk.Button(login_frame, text="Login", font=("Arial", 14), width=10, bg="#0047ab", fg="white", command=login)
login_button.place(relx=0.5, y=200, anchor=tk.CENTER)

# Top Right: Why Choose Us?
benefits_frame = tk.Frame(root, bg="#f7f7f7", width=400, height=200, relief="solid", borderwidth=1)
benefits_frame.place(x=520, y=70)

benefits_label = tk.Label(benefits_frame, text="Why Choose Us?", font=("Arial", 18, "bold"), bg="#f7f7f7", fg="#0047ab")
benefits_label.pack(anchor="w", padx=10, pady=10)

benefits_text = """• Secure online banking.
• Manage your accounts with ease.P
• 24/7 customer support.
• Comprehensive financial tools."""
benefits_content = tk.Label(benefits_frame, text=benefits_text, font=("Arial", 14), bg="#f7f7f7", fg="black", justify="left")
benefits_content.pack(anchor="w", padx=10)

# Bottom Left: Latest Updates
news_frame = tk.Frame(root, bg="#f7f7f7", width=400, height=200, relief="solid", borderwidth=1)
news_frame.place(x=20, y=330)

news_label = tk.Label(news_frame, text="Latest Updates", font=("Arial", 18, "bold"), bg="#f7f7f7", fg="#0047ab")
news_label.pack(anchor="w", padx=10, pady=10)

news_text = """• New mobile app features released.
• Updated terms of service for 2024.
• Holiday banking hours extended."""
news_content = tk.Label(news_frame, text=news_text, font=("Arial", 14), bg="#f7f7f7", fg="black", justify="left")
news_content.pack(anchor="w", padx=10)

# Bottom Right: Testimonials
testimonials_frame = tk.Frame(root, bg="#f7f7f7", width=400, height=200, relief="solid", borderwidth=1)
testimonials_frame.place(x=520, y=330)

testimonials_label = tk.Label(testimonials_frame, text="What Our Customers Say", font=("Arial", 18, "bold"), bg="#f7f7f7", fg="#0047ab")
testimonials_label.pack(anchor="w", padx=10, pady=10)

testimonial_text = """• "Best online banking experience ever!" - Alex
• "Super secure and easy to use." - Jamie
• "I love the cashback rewards!" - Taylor"""
testimonials_content = tk.Label(testimonials_frame, text=testimonial_text, font=("Arial", 14), bg="#f7f7f7", fg="black", justify="left")
testimonials_content.pack(anchor="w", padx=10)

# Footer Bar: Quick Access
footer_frame = tk.Frame(root, bg="#0047ab", height=50)
footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

quick_access_label = tk.Label(footer_frame, text="Quick Access", font=("Arial", 14, "bold"), bg="#0047ab", fg="white")
quick_access_label.pack(side=tk.LEFT, padx=10)

buttons = [("Open New Account", lambda: print("New Account")),
           ("Transfer Funds", lambda: print("Transfer")),
           ("Contact Support", lambda: print("Support"))]

for text, command in buttons:
    button = tk.Button(footer_frame, text=text, font=("Arial", 12), bg="#0047ab", fg="white", command=command, width=20, borderwidth=0)
    button.pack(side=tk.LEFT, padx=10)

root.mainloop()
