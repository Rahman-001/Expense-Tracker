import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import csv
import os

# CSV file setup
FILE_NAME = "expenses.csv"
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Amount", "Category", "Note"])

# GUI setup
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x500")

# Labels and entries
tk.Label(root, text="Amount (₹):").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Label(root, text="Category:").pack()
entry_category = tk.Entry(root)
entry_category.pack()

tk.Label(root, text="Note:").pack()
entry_note = tk.Entry(root)
entry_note.pack()

# Add expense function
def add_expense():
    amount = entry_amount.get()
    category = entry_category.get()
    note = entry_note.get()
    date = datetime.now().strftime("%Y-%m-%d")

    if not amount or not category:
        messagebox.showerror("Error", "Amount and category are required.")
        return

    try:
        float(amount)  # Validate amount
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number.")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, note])

    entry_amount.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_note.delete(0, tk.END)
    messagebox.showinfo("Success", "Expense added successfully!")

# View expenses function
def view_expenses():
    text_display.delete("1.0", tk.END)
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            text_display.insert(tk.END, " | ".join(row) + "\n")

# Total expenses function
def total_expenses():
    total = 0
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            total += float(row[1])
    messagebox.showinfo("Total Expenses", f"Total spent: ₹{total}")

# Buttons
tk.Button(root, text="Add Expense", command=add_expense).pack(pady=5)
tk.Button(root, text="View Expenses", command=view_expenses).pack(pady=5)
tk.Button(root, text="Show Total", command=total_expenses).pack(pady=5)

# Text box to display expenses
text_display = tk.Text(root, height=15, width=50)
text_display.pack(pady=10)

root.mainloop()
