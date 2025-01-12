import tkinter as tk
from view.components.components import CreateTreeview
from controller.insurances_controller import InsurancesController
import tkinter.messagebox as msg


class InsurancesPage(tk.Tk):
    def reset_form(self):
        status, doc_list = InsurancesController.find_all()
        if status:
            self.tree_view.refresh_table(doc_list, [1, 2, 3, 4])

    def left_click_table(self, event):
        selected_id = self.tree_view.table.focus()
        if self.tree_view.table.item(selected_id)["values"]:
            msg.showinfo("", "You need to sign up or login first!")

    def __init__(self):
        super().__init__()

        self.title("Insurances")
        self.geometry("500x450")

        columns_title = ["Services", "Number of duration", "Duration period", "Cost"]
        self.tree_view = CreateTreeview(self, 4, "headings", 125, 450, columns_title, 0, 0, True)
        self.tree_view.table.bind("<ButtonRelease>", self.left_click_table)

        self.reset_form()
        self.mainloop()


class InsuranceBuy(InsurancesPage):
    def buy_key(self):
        # TODO:
        pass

    def cancel_key(self):
        self.buy_page.destroy()
        self.destroy()

    def left_click_table(self, event):
        selected_id = self.tree_view.table.focus()
        print(self.tree_view.table.item(selected_id))
        if self.tree_view.table.item(selected_id)["values"]:
            # Creating buy page
            self.buy_page = tk.Tk()
            self.buy_page.geometry("400x100")
            self.buy_page.title("Buy Insurance")
            bg_color = "light cyan"
            self.buy_page.configure(bg=bg_color)
            text = "Are you sure you want to buy this service?"
            tk.Label(self.buy_page, text=text, bg=bg_color, font=("Arial", 14)).place(x=10, y=10)

            # Buy key
            buy_button = tk.Button(self.buy_page, text="Buy", width=15, bg=bg_color, command=self.buy_key)
            buy_button.place(x=200, y=60)

            # Cancel key
            cancel_button = tk.Button(self.buy_page, text="Cancel", width=15, bg=bg_color, command=self.cancel_key)
            cancel_button.place(x=70, y=60)

            self.buy_page.mainloop()

    def __init__(self):
        super().__init__()
        self.buy_page = None
