import tkinter as tk

def label(root: tk, text_label: str, bg_color: str, f_family: str, f_size: int):
    '''Defines a syntax to create a Label element'''
    element = tk.Label(
        root,
        text=text_label,
        bg=bg_color,
        font=(f_family, f_size),
        wraplength=500
    )
    return element

def entry(root: tk, bg_color: str, f_family: str, f_size: int, h_thick: int, h_bg: str, h_color: str):
    '''Defines a syntax to create an Entry element'''
    element = tk.Entry(
        root,
        bg=bg_color,
        font=(f_family, f_size),
        highlightthickness=h_thick,
        highlightbackground=h_bg,
        highlightcolor=h_color
    )
    return element

def button(root: tk, text_label: str, func, fg_color: str, bg_color: str, f_family: str, f_size: int, type: str, active_fg: str = None, active_bg: str = None):
    '''Defines a syntax to create a Button element'''
    element = tk.Button(
        root,
        text=text_label,
        command=func,
        fg=fg_color, 
        bg=bg_color, 
        font=(f_family, f_size),
        bd=1,
        padx=15,
        relief=type,
        activeforeground=active_fg, 
        activebackground=active_bg
    )
    return element