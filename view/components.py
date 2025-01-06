from tkinter import *
import tkinter.ttk


class CreateTreeview:
    def refresh_table(self, data_list, column_id=None):
        for item in self.table.get_children():
            self.table.delete(item)

        if not column_id:
            if data_list:
                for data in data_list:
                    self.table.insert("", END, values=tuple(data[1:]))
        else:
            if data_list:
                for data in data_list:
                    self.table.insert("", END, values=tuple(data))

    def __init__(self, master, columns_number, show, columns_width, column_height, column_title, x, y):
        columns = []
        for i in range(columns_number):
            columns.append(i)
        columns = tuple(columns)
        self.table = tkinter.ttk.Treeview(master, columns=columns, show=show, height=column_height)
        for i in range(len(columns)):
            self.table.column(i, width=columns_width)
            self.table.heading(i, text=column_title[i])

        self.table.place(x=x, y=y)


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
