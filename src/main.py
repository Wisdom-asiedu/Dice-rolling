import random
import tkinter as tk
from tkinter import PhotoImage, Label, Text
from src.widget import label, entry, button

roll_history = []
light_blue = '#CEE8FA'

def roll_dice(num_dice, num_sides):
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    total = sum(rolls)
    return rolls, total

def roll_button_clicked(event=None):
    try:
        num_dice = int(num_dice_entry.get())                                                                       # Gets input 
        if num_dice > 0:
            num_sides = int(sides_entry.get())                                                                     # Gets input   
            if num_sides > 0:
                rolls, total = roll_dice(num_dice, num_sides)
                result_text = f"Rolls:\n{', '.join(str(roll) for roll in rolls)}\nTotal: {total}"
                result_label.config(text=result_text, fg='black')                                                  # Outputs results       
                roll_history.append(f"Rolled {num_dice} dice with {num_sides} sides: {rolls}\nTotal: {total}")
            else:                                                                                                  # Handles errors
                result_label.config(text="Cannot roll a die without sides", fg='red')
        else:
            result_label.config(text="The number of dice should be countable", fg='red')
    except ValueError:
        result_label.config(text="Enter a counting number!", fg='red')

def view_history():
    # Creates the View History window
    history_window = tk.Toplevel(root)
    history_window.title("Roll History")
    history_window.iconphoto(False, PhotoImage(file="src/assets/history_favicon.ico"))
    history_window.configure(bg='dark blue')
    history_text = Text(history_window, wrap=tk.WORD, font=("Maiandra GD", 12), fg='dark blue', bg='#F3F5FF')
    history_text.pack(fill="both", expand=True, padx=5, pady=5)

    # Updates the roll list
    for roll in roll_history:
        history_text.insert(tk.END, roll + "\n\n")

def clear_history():
    roll_history.clear()

def on_closing():
    root.quit()  # Terminate the main window
    root.destroy()  # Clean up resources

def start_simulation():
    '''Runs the main app'''
    # Create main window
    global root
    root = tk.Toplevel()
    root.title("Dice Rolling Simulator")
    root.iconphoto(False, PhotoImage(file="src/assets/favicon_main.ico"))
    root.geometry("800x600")
    root.resizable(True, True)
    root.configure(bg=light_blue)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    logo_image = PhotoImage(file="src/assets/logo_main.png")

    # Create widgets
    global num_dice_entry
    global sides_entry
    global result_label

    logo = Label(root, image=logo_image, bg=light_blue)
    text_drs= label(root, "Dice Rolling Simulator", light_blue, "Exotc350 DmBd BT", 42)
    num_dice_label = label(root, "Number of Dice: ", light_blue, "Book Antiqua", 16)
    sides_label = label(root, "Number of Sides: ", light_blue, "Book Antiqua", 16)
    num_dice_entry = entry(root, "white", "Maiandra GD", 12, 1, "dark blue", "blue")
    sides_entry = entry(root, "white", "Maiandra GD", 12, 1, "dark blue", "blue")
    roll_button = button(root, "Roll Dice", roll_button_clicked, "dark blue", "white", "Exotc350 DmBd BT", 16, "solid", "white", "dark blue")
    result_label = label(root, "\n", light_blue, "Constantia", 16)
    view_history_button = button(root, "View History", view_history, "white", "dark blue", "Book Antiqua", 14, "ridge")
    clear_history_button = button(root, "Clear History", clear_history, "black", "red", "Book Antiqua", 14, "sunken")

    # Bind Enter key to roll_button_clicked
    root.bind('<Return>', roll_button_clicked)

    # Layout widgets
    root.columnconfigure(0, weight=1)
    root.columnconfigure(4, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(8, weight=1)

    # Place widgets
    logo.grid(row=1, column=1, columnspan=2)
    text_drs.grid(row=2, column=1, columnspan=2, pady=10)
    num_dice_label.grid(row=3, column=1, pady=5)
    num_dice_entry.grid(row=3, column=2, pady=5)
    sides_label.grid(row=4, column=1, pady=5)
    sides_entry.grid(row=4, column=2, pady=5)
    roll_button.grid(row=5, column=1, columnspan=2, pady=10)
    result_label.grid(row=6, column=1, columnspan=2, pady=10)
    view_history_button.grid(row=8, column=1, columnspan=1)
    clear_history_button.grid(row=8, column=2, columnspan=1)

    # Start the GUI event loop
    root.mainloop()
