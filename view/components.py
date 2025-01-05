from tkinter import *
import tkinter.ttk


class CreateTreeview:
    def __init__(self, master, columns_number, show, columns_width, column_title, x, y):
        columns = []
        for i in range(columns_number):
            columns.append(i)
        columns = tuple(columns)
        table = tkinter.ttk.Treeview(master, columns=columns, show=show)
        for i in range(len(columns)):
            table.column(i, width=columns_width)
            table.heading(i, text=column_title[i])

        table.place(x=x, y=y)


class TextWithLabel:
    def __init__(self, master, text, x, y, data_type="str", key_press_event=None):
        tkinter.Label(master, text=text).place(x=x, y=y)
        match data_type:
            case "str":
                self.value = StringVar()
            case "int":
                self.value = IntVar()
            case "float":
                self.value = DoubleVar()
            case "bool":
                self.value = BooleanVar()
        text_box = tkinter.Entry(master, textvariable=self.value)
        if key_press_event:
            text_box.bind("<KeyRelease>", key_press_event)
        text_box.place(x=x + 120, y=y)