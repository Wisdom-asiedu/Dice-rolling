import random
import tkinter as tk
#from tkinter import PhotoImage
from src.widget import label, entry, button

roll_history = []

def roll_dice(num_dice, sides):
    rolls = [random.randint(1, sides) for _ in range(num_dice)]
    total = sum(rolls)
    return rolls, total

def roll_button_clicked(event=None):
    num_dice = int(num_dice_entry.get())
    sides = int(sides_entry.get())
    rolls, total = roll_dice(num_dice, sides)
    result_text = f"Rolls:\n{', '.join(str(roll) for roll in rolls)}\nTotal: {total}"
    result_label.config(text=result_text)
    roll_history.append(f"Rolled {num_dice} dice with {sides} sides: {rolls}\nTotal: {total}")

def clear_history():
    roll_history.clear()
        
def view_history():
    history_window = tk.Toplevel(root)
    history_window.title("Roll History")
    history_window.configure(bg='dark blue')
    #history_window.iconphoto(False, PhotoImage(file="src/assets/history_favicon.png"))
    history_window.wm_iconbitmap("src/assets/favicon.ico")  
    history_text = tk.Text(history_window, wrap=tk.WORD, font=("Maiandra GD", 12), fg='dark blue', bg='#ffe')
    history_text.pack(padx=5, pady=5)
    for roll in roll_history:
        history_text.insert(tk.END, roll + "\n\n")

def on_closing():
    root.quit()  # Terminate the main window
    root.destroy()  # Clean up resources
    
def start_simulation():
    # Create main window
    global root
    root = tk.Tk()
    root.title("Dice Rolling Simulator")
    root.geometry("800x600")
    root.resizable(True, True)
    root.configure(bg='light blue')
    #root.iconphoto(True, PhotoImage(file="src/assets/favicon.ico"))
    root.wm_iconbitmap("src/assets/favicon.ico")  
    root.protocol("WM_DELETE_WINDOW", on_closing)  # Bind the on_closing function to the window close event


    # Create widgets
    global num_dice_entry
    global sides_entry
    global result_label
    num_dice_label = label(root, "Number of Dice: ", "light blue", "Book Antiqua", 16)
    sides_label = label(root, "Number of Dice: ", "light blue", "Book Antiqua", 16)
    num_dice_entry = entry(root, "white", "Maiandra GD", 12, 1, "dark blue", "blue")
    sides_entry = entry(root, "white", "Maiandra GD", 12, 1, "dark blue", "blue")
    roll_button = button(root, "Roll Dice", roll_button_clicked, "dark blue", "white", "Exotc350 DmBd BT", 16, "solid", "white", "dark blue")
    result_label = label(root, "\n", "light blue", "Constantia", 16)
    view_history_button = button(root, "View History", view_history, "white", "dark blue", "Book Antiqua", 14, "ridge")
    clear_history_button = button(root, "Clear History", clear_history, "black", "red", "Book Antiqua", 14, "sunken")

    # Bind Enter key to roll_button_clicked
    root.bind('<Return>', roll_button_clicked)

    # Layout widgets
    root.columnconfigure(0, weight=1)
    root.columnconfigure(4, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(7, weight=1)

    num_dice_label.grid(row=1, column=1, pady=5)
    num_dice_entry.grid(row=1, column=2, pady=5)
    sides_label.grid(row=2, column=1, pady=5)
    sides_entry.grid(row=2, column=2, pady=5)
    roll_button.grid(row=3, column=1, columnspan=2, pady=10)
    result_label.grid(row=4, column=1, columnspan=2, pady=10)
    view_history_button.grid(row=7, column=1, columnspan=1)
    clear_history_button.grid(row=7, column=2, columnspan=1)

    # Start the GUI event loop
    root.mainloop()