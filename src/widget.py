import tkinter as tk

'''def create_widgets(root):

    # Create widgets
    num_dice_label = tk.Label(root, text="Number of Dice:", bg='light blue', font=("Book Antiqua", 16))
    num_dice_entry = tk.Entry(root, bg='white', font=("Maiandra GD", 12, 'bold'), highlightthickness=1, highlightbackground="dark blue", highlightcolor="blue")
    sides_label = tk.Label(root, text="Number of Sides:", bg='light blue', font=("Book Antiqua", 16))
    sides_entry = tk.Entry(root, bg='white', font=("Maiandra GD", 12, 'bold'), highlightthickness=1, highlightbackground="dark blue", highlightcolor="blue")
    roll_button = tk.Button(root, text="Roll Dice", fg='dark blue', bg='white', font=("Book Antiqua", 14), bd=1, padx=5, relief='solid', activeforeground="white", activebackground="dark blue")
    result_label = tk.Label(root, text="\n", bg='light blue', wraplength=500, font=("Constantia", 16))
    view_history_button = tk.Button(root, text="View History", fg='white', bg='dark blue', font=("Book Antiqua", 12, 'bold'), padx=5, bd=1, relief="ridge")
    clear_history_button = tk.Button(root, text="Clear History", bg='red', font=("Book Antiqua", 12, 'bold'), padx=5, bd=1, relief="sunken")

    return (num_dice_label, num_dice_entry, sides_label, sides_entry, roll_button,
            result_label, view_history_button, clear_history_button)'''

def label(root: tk, text_label: str, bg_color: str, f_family: str, f_size: int):
    element = tk.Label(root,
                       text=text_label,
                       bg=bg_color,
                       font=(f_family, f_size)
                       )
    return element

def entry(root: tk, bg_color: str, f_family: str, f_size: int, h_thick: int, h_bg: str, h_color: str):
    element = tk.Entry(root,
                       bg=bg_color,
                       font=(f_family, f_size),
                       highlightthickness=h_thick,
                       highlightbackground=h_bg,
                       highlightcolor=h_color
                       )
    return element

def button(root: tk, text_label: str, func, fg_color: str, bg_color: str, f_family: str, f_size: int, type: str, a_fg : str, a_bg: str):
    element = tk.Button(root,
                        text=text_label,
                        command=func,
                        fg=fg_color, 
                        bg=bg_color, 
                        font=(f_family, f_size),
                        bd=1,
                        padx=5,
                        relief=type,
                        activeforeground=a_fg, 
                        activebackground=a_bg
                        )
    return element