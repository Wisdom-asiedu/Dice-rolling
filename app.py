import tkinter as tk
from tkinter import PhotoImage, Label
import src.main as app
from src.widget import label, button

def start_sim():
    root.withdraw()  # Hide the intro window
    app.start_simulation()  # Start the main window
    root.quit()  # Exit the application when main window is closed

def quit_sim():
    root.quit()  # Exit the application

# Create the window
root = tk.Tk()
root.title("Dice Rolling Simulator")
root.iconphoto(False, PhotoImage(file="src/assets/favicon.ico"))
root.geometry("800x600")
root.resizable(True, True)
root.configure(bg=app.light_blue)

# Create the widgets
logo_image = PhotoImage(file="src/assets/logo_intro.png")
logo_label = Label(root, image=logo_image, bg=app.light_blue)
text_welcome = label(root, "Welcome", app.light_blue, "Script MT Bold", 30)
text_to = label(root, "to", app.light_blue, "Script MT Bold", 12)
text_drs= label(root, "Dice Rolling Simulator", app.light_blue, "Exotc350 DmBd BT", 42)
start_button = button(root, "Start", start_sim, "white", "dark blue", "Exotc350 DmBd BT", 16, "raise")
quit_button = button(root, "Quit", quit_sim, "white", "red", "Exotc350 DmBd BT", 16, "ridge")

# Layout widgets
root.columnconfigure(0, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(7, weight=1)

# Placce widgets
text_welcome.grid(row=1, column=1)
text_to.grid(row=2, column=1)
text_drs.grid(row=3, column=1)
logo_label.grid(row=4, column=1, pady=5)
start_button.grid(row=5, column=1, pady=30)
quit_button.grid(row=6, column=1, pady=5)

# Start the intro window loop
root.mainloop()