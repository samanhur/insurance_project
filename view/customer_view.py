import tkinter as tk

from model.da.insurance_list_da import InsuranceListDa
from view.components.components import TextWithLabel, CreateTreeview
from view.insurances_page import InsuranceBuy


class CustomerPage(tk.Tk):

    def reset_form(self):
        status, doc_list = InsuranceListDa.find_by_status(self.customer_id)
        if status:
            self.tree_view.refresh_table(doc_list, [1, 2, 3, 5])

    def edit(self):
        print("edit")

    def insurances(self):
        insurance_customer = InsuranceBuy()

    def __init__(self, customer_info):
        super().__init__(None)

        self.title("Customer Page")
        self.geometry("780x500")
        bg_color = "light cyan"
        self.configure(bg=bg_color)

        self.label = tk.Label(self, text="Dashboard", bg=bg_color, font=("Arial", 20))
        self.label.place(x=20, y=10)

        self.customer_info = customer_info
        self.customer_id = self.customer_info.person_id

        self.name = TextWithLabel(self, "Name:", 20, 60, bg_color, 120, state=True)
        self.family = TextWithLabel(self, "Family:", 20, 100, bg_color, 120, state=True)
        self.father_name = TextWithLabel(self, "Father name:", 20, 140, bg_color, 120, state=True)
        self.national_code = TextWithLabel(self, "National code:", 20, 180, bg_color, 120, state=True)
        self.birth_date = TextWithLabel(self, "Birth date:", 20, 220, bg_color, 120, state=True)
        self.phone = TextWithLabel(self, "Phone:", 20, 260, bg_color, 120)
        self.username = TextWithLabel(self, "Username:", 20, 300, bg_color, 120, state=True)
        self.password = TextWithLabel(self, "Password:", 20, 340, bg_color, 120)

        self.edit_button = tk.Button(self, text="Edit", width=34, bg=bg_color, command=self.edit)
        self.edit_button.place(x=20, y=400)

        self.edit_button = tk.Button(self, text="Insurances", width=34, bg=bg_color, command=self.insurances)
        self.edit_button.place(x=20, y=450)

        # active services table
        self.services = tk.Label(self, text="Active services", bg=bg_color, font=("Arial", 14))
        self.services.place(x=300, y=15)

        columns_title = ["Services", "Number of duration", "Duration period", "Expire at"]
        self.tree_view = CreateTreeview(self, 4, "headings", 115, 14, columns_title, 300, 55, False)

        self.reset_form()

        self.mainloop()


# customer_page = CustomerPage()
