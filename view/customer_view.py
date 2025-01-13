import tkinter as tk

from controller.active_insurances_controller import ActiveInsuranceController
from view.components.components import TextWithLabel, CreateTreeview
from view.insurances_page import InsuranceBuy


class CustomerPage(tk.Tk):

    def reset_form(self):
        status, doc_list = ActiveInsuranceController.find_by_expire_date(self.customer_id)
        if status:
            self.tree_view.refresh_table(doc_list, [0, 1, 2, 3, 5])

    def edit(self):
        print("edit")

    def insurances(self):
        InsuranceBuy(self.customer_id)

    def customer_set_info(self):
        self.name.value.set(self.customer_info.name)
        self.family.value.set(self.customer_info.family)
        self.father_name.value.set(self.customer_info.father_name)
        self.father_name.value.set(self.customer_info.father_name)
        self.national_code.value.set(self.customer_info.national_code)
        self.birth_date.value.set(self.customer_info.birth_date)
        self.phone.value.set(self.customer_info.phone)
        self.username.value.set(self.customer_info.username)
        self.password.value.set(self.customer_info.password)

    def update_insurance_list(self):
        self.reset_form()

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

        # Buttons
        self.edit_button = tk.Button(self, text="Edit", width=34, bg=bg_color, command=self.edit)
        self.edit_button.place(x=20, y=400)

        self.insurances_button = tk.Button(self, text="Insurances", width=34, bg=bg_color, command=self.insurances)
        self.insurances_button.place(x=20, y=450)

        self.update_insurance_list_button = tk.Button(
            self, text="Update Insurance List", width=65, bg=bg_color, command=self.update_insurance_list
        )
        self.update_insurance_list_button.place(x=300, y=450)

        # active services table
        self.services = tk.Label(self, text="Active services", bg=bg_color, font=("Arial", 14))
        self.services.place(x=300, y=15)

        columns_title = ["Services", "Number of duration", "Duration period", "Expire at"]
        self.tree_view = CreateTreeview(self, 4, "headings", 115, 14, columns_title, 300, 55, False)

        self.reset_form()

        self.customer_set_info()

        self.mainloop()
