import tkinter as tk
from components import CreateTreeview
from controller.insurances_controller import InsurancesController


class InsurancesPage(tk.Tk):

    def reset_form(self):
        status, doc_list = InsurancesController.find_all()
        if status:
            self.tree_view.refresh_table(doc_list)

    def __init__(self):
        super().__init__()

        self.title("Insurances")
        self.geometry("500x450")

        columns_title = ["Services", "Number of duration", "Duration period", "Cost"]
        self.tree_view = CreateTreeview(self, 4, "headings", 125, 450, columns_title, 0, 0)

        self.reset_form()
        self.mainloop()
