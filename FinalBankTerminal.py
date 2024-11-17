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

# Fetch user account information from environment variables
user_accounts = {
    "user1": {
        "checking_balance": os.getenv("USER1_CHECKING_BALANCE"),
        "savings_balance": os.getenv("USER1_SAVINGS_BALANCE"),
        "credit_card_balance": os.getenv("USER1_CREDIT_CARD_BALANCE"),
        "routing_number": os.getenv("USER1_ROUTING_NUMBER"),
        "account_number": os.getenv("USER1_ACCOUNT_NUMBER")
    },
    "user4": {
        "checking_balance": os.getenv("USER4_CHECKING_BALANCE"),
        "savings_balance": os.getenv("USER4_SAVINGS_BALANCE"),
        "credit_card_balance": os.getenv("USER4_CREDIT_CARD_BALANCE"),
        "routing_number": os.getenv("USER4_ROUTING_NUMBER"),
        "account_number": os.getenv("USER4_ACCOUNT_NUMBER")
    },
    "user7": {
        "checking_balance": os.getenv("USER7_CHECKING_BALANCE"),
        "savings_balance": os.getenv("USER7_SAVINGS_BALANCE"),
        "credit_card_balance": os.getenv("USER7_CREDIT_CARD_BALANCE"),
        "routing_number": os.getenv("USER7_ROUTING_NUMBER"),
        "account_number": os.getenv("USER7_ACCOUNT_NUMBER")
    },
    "user3": {
        "checking_balance": os.getenv("USER3_CHECKING_BALANCE"),
        "savings_balance": os.getenv("USER3_SAVINGS_BALANCE"),
        "credit_card_balance": os.getenv("USER3_CREDIT_CARD_BALANCE"),
        "routing_number": os.getenv("USER3_ROUTING_NUMBER"),
        "account_number": os.getenv("USER3_ACCOUNT_NUMBER")
    },
    "user6": {
        "checking_balance": os.getenv("USER6_CHECKING_BALANCE"),
        "savings_balance": os.getenv("USER6_SAVINGS_BALANCE"),
        "credit_card_balance": os.getenv("USER6_CREDIT_CARD_BALANCE"),
        "routing_number": os.getenv("USER6_ROUTING_NUMBER"),
        "account_number": os.getenv("USER6_ACCOUNT_NUMBER")
    }
}

def show_info_page(title, content):
    # Clear the existing content in the root window
    for widget in root.winfo_children():
        widget.destroy()

    # Create the info page layout
    root.title(title)
    root.configure(bg="#f7f7f7")

    # Display title
    title_label = tk.Label(root, text=title, font=("Arial", 18, "bold"), bg="#f7f7f7", fg="#0047ab")
    title_label.pack(pady=10)

    # Display content
    content_label = tk.Label(root, text=content, font=("Arial", 14), bg="#f7f7f7", fg="black", justify="left")
    content_label.pack(padx=20, pady=10)

    # Add back button
    back_button = tk.Button(root, text="Back", font=("Arial", 14), bg="#0047ab", fg="white", command=show_main_page)
    back_button.pack(pady=20)

def show_account_page(username):
    # Fetch account information for the logged-in user
    account_info = user_accounts.get(username, {})

    # Prepare account information content
    content = f"""
    Checking Balance: {account_info.get('checking_balance', 'N/A')}
    Savings Balance: {account_info.get('savings_balance', 'N/A')}
    Credit Card Balance: {account_info.get('credit_card_balance', 'N/A')}
    Routing Number: {account_info.get('routing_number', 'N/A')}
    Account Number: {account_info.get('account_number', 'N/A')}
    """
    show_info_page(f"{username.capitalize()}'s Account Information", content)

def show_main_page():
    global username_entry, password_entry, error_label
    # Clear the existing content in the root window
    for widget in root.winfo_children():
        widget.destroy()

    # Rebuild the main page layout
    root.title("Bank Terminal Login")
    root.geometry("900x600")
    root.configure(bg="#f7f7f7")

    # Create the top header bar
    header_frame = tk.Frame(root, bg="#0047ab", height=50)
    header_frame.pack(fill=tk.X, side=tk.TOP)

    # Add a bank logo placeholder
    logo_label = tk.Label(header_frame, text="BANK OF PYTHON", font=("Arial", 16, "bold"), bg="#0047ab", fg="white")
    logo_label.pack(side=tk.LEFT, padx=10)

    # Add navigation links
    nav_links = [
        ("Checking", "Information about Checking Accounts."),
        ("Savings & CDs", "Information about Savings Accounts and CDs."),
        ("Credit Cards", "Information about Credit Cards."),
        ("Home Loans", "Information about Home Loans."),
        ("Auto Loans", "Information about Auto Loans."),
        ("Investing", "Information about Investing Opportunities."),
        ("Security", "Information about Security and Fraud Protection.")
    ]

    for link, content in nav_links:
        nav_button = tk.Button(header_frame, text=link, font=("Arial", 12), bg="#0047ab", fg="white", borderwidth=0,
                               command=lambda l=link, c=content: show_info_page(l, c))
        nav_button.pack(side=tk.LEFT, padx=10)

    # Top Left: Login Box
    login_frame = tk.Frame(root, bg="#d71a1a", width=400, height=250, relief="solid", borderwidth=1)
    login_frame.place(x=20, y=70)

    login_label = tk.Label(login_frame, text="Login to Your Account", font=("Arial", 18), bg="#d71a1a", fg="white")
    login_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    error_label = tk.Label(login_frame, text="", font=("Arial", 12), bg="#d71a1a", fg="white")
    error_label.place(x=43, y=57)

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
    benefits_frame.place(x=510, y=120)

    benefits_label = tk.Label(benefits_frame, text="Why Choose Us?", font=("Arial", 18, "bold"), bg="#f7f7f7", fg="#0047ab")
    benefits_label.pack(anchor="w", padx=10, pady=10)

    benefits_text = """• Secure online banking.
• Manage your accounts with ease.
• 24/7 customer support.
• Comprehensive financial tools."""
    benefits_content = tk.Label(benefits_frame, text=benefits_text, font=("Arial", 14), bg="#f7f7f7", fg="black", justify="left")
    benefits_content.pack(anchor="w", padx=10)

    # Bottom Left: Latest Updates
    news_frame = tk.Frame(root, bg="#f7f7f7", width=400, height=200, relief="solid", borderwidth=1)
    news_frame.place(x=50, y=370)

    news_label = tk.Label(news_frame, text="Latest Updates", font=("Arial", 18, "bold"), bg="#f7f7f7", fg="#0047ab")
    news_label.pack(anchor="w", padx=10, pady=10)

    news_text = """• New mobile app features released.
• Updated terms of service for 2024.
• Holiday banking hours extended."""
    news_content = tk.Label(news_frame, text=news_text, font=("Arial", 14), bg="#f7f7f7", fg="black", justify="left")
    news_content.pack(anchor="w", padx=10)

    # Bottom Right: Testimonials
    testimonials_frame = tk.Frame(root, bg="#f7f7f7", width=400, height=200, relief="solid", borderwidth=1)
    testimonials_frame.place(x=450, y=370)

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

    buttons = [
        ("Open New Account", "Information on how to open a new account."),
        ("Transfer Funds", "Instructions for transferring funds between accounts."),
        ("Contact Support", "Contact us at:\nPhone: 1-800-555-1234\nEmail: support@bankofpython.com")
    ]

    for text, content in buttons:
        button = tk.Button(footer_frame, text=text, font=("Arial", 12), bg="#0047ab", fg="white", command=lambda t=text, c=content: show_info_page(t, c), width=20, borderwidth=0)
        button.pack(side=tk.LEFT, padx=10)

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Clear previous error message
    error_label.config(text="")

    if username in hashed_credentials and hashed_credentials[username] is not None:
        if bcrypt.checkpw(password.encode(), hashed_credentials[username]):
            print("Password Correct")
            show_account_page(username)
        else:
            error_label.config(fg="white", text="Login Failed: Invalid username or password.")
            password_entry.delete(0, tk.END)
    else:
        error_label.config(fg="white", text="Login Failed: Invalid username or password.")
        password_entry.delete(0, tk.END)

# Initialize the main page
root = tk.Tk()
show_main_page()
root.mainloop()
