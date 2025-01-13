import tkinter as tk

from controller.employee_controller import EmployeeController
from controller.insurances_controller import InsurancesController


class AdminPage(tk.Tk):
    def reset_insurance_form(self):
        status, doc_list = InsurancesController.find_all()
        if status:
            self.insurance_list.refresh_table(doc_list, [1, 2, 3, 4])

    def reset_employee_form(self):
        status, doc_list = EmployeeController.find_all()
        if status:
            self.insurance_list.refresh_table(doc_list, [0, 3, 5, 8])

    def __init__(self):
        super().__init__()

        self.title("Admin Page")
        self.geometry("800x500")
        bg_color = "light cyan"
        self.configure(bg=bg_color)
        self.employee_main_frame = tk.Frame(self, bg=bg_color, highlightbackground="black", highlightthickness=1,
                                            width=400,
                                            height=500)
        self.employee_main_frame.place(x=0, y=0)

        # Create employee controller
        self.employee_frame = tk.Frame(self, bg=bg_color, highlightbackground="black", highlightthickness=1, width=400,
                                       height=115)
        self.employee_frame.place(x=0, y=0)

        self.employee_label = tk.Label(self, text="Employee", bg=bg_color, font=("Arial", 18))
        self.employee_label.place(x=10, y=10)

        self.add_employee_key = tk.Button(self, text="Add", bg=bg_color, width=10)
        self.add_employee_key.place(x=40, y=60)

        self.edit_employee_key = tk.Button(self, text="Edit", bg=bg_color, width=10)
        self.edit_employee_key.place(x=140, y=60)

        self.remove_employee_key = tk.Button(self, text="Remove", bg=bg_color, width=10)
        self.remove_employee_key.place(x=240, y=60)

        # Employee list
        columns_title = ["Id", "National code", "Username", "Role"]
        self.insurance_list = CreateTreeview(self, 4, "headings", 100, 50, columns_title, 0, 115)

        self.reset_employee_form()

        # Create insurances controller
        self.insurance_frame = tk.Frame(self, bg=bg_color, highlightbackground="black", highlightthickness=1, width=400,
                                        height=115)
        self.insurance_frame.place(x=400, y=0)

        self.insurance_label = tk.Label(self, text="Insurances", bg=bg_color, font=("Arial", 18))
        self.insurance_label.place(x=410, y=10)

        self.add_insurance_key = tk.Button(self, text="Add", bg=bg_color, width=10)
        self.add_insurance_key.place(x=440, y=60)

        self.edit_insurance_key = tk.Button(self, text="Edit", bg=bg_color, width=10)
        self.edit_insurance_key.place(x=540, y=60)

        self.delete_insurance_key = tk.Button(self, text="Delete", bg=bg_color, width=10)
        self.delete_insurance_key.place(x=640, y=60)

        # Insurance list
        columns_title = ["Services", "Number of duration", "Duration period", "Cost"]
        self.insurance_list = CreateTreeview(self, 4, "headings", 100, 50, columns_title, 400, 115)

        self.reset_insurance_form()

        self.mainloop()
