from tkinter import *
import tkinter.ttk


class CreateTreeview:
    def refresh_table(self, data_list, values_number):
        for item in self.table.get_children():
            self.table.delete(item)

        # Is there any better way to do this?
        # I can do this just for this project!
        # I can code a condition that specifies this tree view will show in what page!
        value_list = []
        for item in data_list:
            values = []
            for n, v in enumerate(item):
                if n in values_number:
                    values.append(v)
            value_list.append(tuple(values))

        if value_list:
            for values in value_list:
                self.table.insert("", END, tags=values[0], values=tuple(values[1:]))

    def left_click_table(self, event):
        selected_item = self.table.focus()
        if self.table.item(selected_item):
            pass

    def __init__(self, master, columns_number, show, columns_width, column_height, column_title, x, y, clickable=True):
        columns = []
        for i in range(columns_number):
            columns.append(i)
        columns = tuple(columns)
        self.table = tkinter.ttk.Treeview(master, columns=columns, show=show, height=column_height)
        for i in range(len(columns)):
            self.table.column(i, width=columns_width)
            self.table.heading(i, text=column_title[i])

        self.table.place(x=x, y=y)

        if clickable:
            self.table.bind("<ButtonRelease>", self.left_click_table)


class TextWithLabel:
    def __init__(self, master, text, x, y, bg_color, distance, data_type="str", state=FALSE, key_press_event=None):
        tkinter.Label(master, text=text, bg=bg_color).place(x=x, y=y)

        match data_type:
            case "str":
                self.value = StringVar()
            case "int":
                self.value = IntVar()
            case "float":
                self.value = DoubleVar()
            case "bool":
                self.value = BooleanVar()

        if state:
            text_box = tkinter.Entry(master, textvariable=self.value, state="readonly")
        else:
            text_box = tkinter.Entry(master, textvariable=self.value)

        if key_press_event:
            text_box.bind("<TreeviewSelect>", key_press_event)

        text_box.place(x=x + distance, y=y)
