import tkinter as tk
class Button1(tk.Button):
    def __init__(self, master=None, **kwargs):
        # Set default options
        options = {
            'bg': '#abc8f5',
            'activebackground': '#abb0f5',
            'cursor': 'boat',
            'fg': 'white',
            'width': 10,
            'height': 1,
            'bd': 2,
            'relief': 'solid',

        }
        # Update options with any arguments passed
        options.update(kwargs)
        super().__init__(master, **options)

class Label1(tk.Label):
    def __init__(self, master=None, **kwargs):
        # Set default options
        options = {
            'bg': '#abc8f5',
            'fg': 'white',
            'font': 'Helvetica 10 bold',
            'width': master.winfo_screenwidth(),
            'height': 1
            # 'borderwidth': 2
            # 'relief': 'flat',
            # 'highlightcolor': 'white'
        }
        # Update options with any arguments passed
        options.update(kwargs)
        super().__init__(master, **options)

class Entry1(tk.Entry):
    def __init__(self, master=None, **kwargs):
        # Set default options
        options = {
            'bg': '#ceddf5',
            'fg': 'black',
            'width': master.winfo_screenwidth(),
            'borderwidth': 1,
            'relief': 'sunken',
            # 'highlightcolor': 'white'
        }
        # Update options with any arguments passed
        options.update(kwargs)
        super().__init__(master, **options)