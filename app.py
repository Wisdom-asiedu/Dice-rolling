import tkinter as tk
from tkinter import PhotoImage
import src.main
from src.widget import label, button

def start_sim():
    root.withdraw()  # Hide the intro window
    src.main.start_simulation()  # Start the main window
    root.quit()  # Exit the application when main window is closed

def quit_sim():
    root.quit()  # Exit the application

# Create the window
root = tk.Tk()
root.title("Dice Rolling Simulator")
root.geometry("800x600")
root.resizable(False, False)  # Disable window resizing
root.configure(bg='light blue')
root.iconphoto(False, PhotoImage(file="src/assets/favicon.ico"))

# Create the widgets
welcome = label(root, "Welcome", "light blue", "Script MT Bold", 30)
to = label(root, "to", "light blue", "Script MT Bold", 12)
drs= label(root, "Dice Rolling Simulator", "light blue", "Exotc350 DmBd BT", 36)
start_button = button(root, "Start", start_sim, "white", "dark blue", "Exotc350 DmBd BT", 16, "raise")
quit_button = button(root, "Quit", quit_sim, "white", "red", "Exotc350 DmBd BT", 16, "ridge")

root.columnconfigure(0, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(6, weight=2)

welcome.grid(row=1, column=1)
to.grid(row=2, column=1)
drs.grid(row=3, column=1)
start_button.grid(row=4, column=1, pady=40)
quit_button.grid(row=5, column=1, pady=5)

# Start the intro window loop
root.mainloop()