import tkinter as tk

from controller.insurances_controller import InsurancesController


class EmployeePage(tk.Tk):
    def reset_form(self):
        status, doc_list = InsurancesController.find_all()
        if status:
            self.insurance_list.refresh_table(doc_list, [1, 2, 3, 4])

    def __init__(self):
        super().__init__()
        # self.employee_info = employee_info

        self.title("Employee Page")
        self.geometry("500x500")
        bg_color = "light cyan"
        self.configure(bg=bg_color)
        self.main_frame = tk.Frame(self, bg=bg_color, highlightbackground="black", highlightthickness=1, width=500,
                                   height=500)
        self.main_frame.place(x=0, y=0)

        # Create customer controller
        self.customer_frame = tk.Frame(self, bg=bg_color, highlightbackground="black", highlightthickness=1, width=500,
                                       height=115)
        self.customer_frame.place(x=0, y=0)

        self.customer_label = tk.Label(self, text="Customer", bg=bg_color, font=("Arial", 18))
        self.customer_label.place(x=10, y=10)

        self.add_customer_key = tk.Button(self, text="Add", bg=bg_color, width=15)
        self.add_customer_key.place(x=40, y=60)

        self.edit_customer_key = tk.Button(self, text="Edit", bg=bg_color, width=15)
        self.edit_customer_key.place(x=190, y=60)

        self.deactive_customer_key = tk.Button(self, text="Deactive", bg=bg_color, width=15)
        self.deactive_customer_key.place(x=340, y=60)

        # Create insurances controller
        self.insurance_frame = tk.Frame(self, bg=bg_color, highlightbackground="black", highlightthickness=1, width=500,
                                        height=115)
        self.insurance_frame.place(x=0, y=115)

        self.insurance_label = tk.Label(self, text="Insurances", bg=bg_color, font=("Arial", 18))
        self.insurance_label.place(x=10, y=125)

        self.add_insurance_key = tk.Button(self, text="Add", bg=bg_color, width=15)
        self.add_insurance_key.place(x=40, y=185)

        self.edit_insurance_key = tk.Button(self, text="Edit", bg=bg_color, width=15)
        self.edit_insurance_key.place(x=190, y=185)

        self.delete_insurance_key = tk.Button(self, text="Delete", bg=bg_color, width=15)
        self.delete_insurance_key.place(x=340, y=185)

        # Insurance List
        columns_title = ["Services", "Number of duration", "Duration period", "Cost"]
        self.insurance_list = CreateTreeview(self, 4, "headings", 125, 50, columns_title, 0, 230)

        self.reset_form()

        self.mainloop()
