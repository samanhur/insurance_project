import tkinter as tk
import tkinter.messagebox as msg

from controller.admin_controller import AdminController
from controller.customer_controller import CustomerController
from controller.employee_controller import EmployeeController
from view.admin_view import AdminPage
from view.components.components import TextWithLabel
from view.customer_view import CustomerPage
from view.employee_view import EmployeePage


class LoginPage(tk.Tk):
    def login_admin(self):
        status = AdminController.find_by_username_and_password(
            self.username_entry.value.get(),
            self.password_entry.value.get(),
        )
        if status:
            self.destroy()
            AdminPage()
        else:
            msg.showerror("login Error", "Username or Password is not correct!")

    def login_employee(self):
        status = EmployeeController.find_by_username_and_password(
            self.username_entry.value.get(),
            self.password_entry.value.get(),
        )
        if status:
            self.destroy()
            # EmployeePage(employee)
            EmployeePage()
        else:
            msg.showerror("login Error", "Username or Password is not correct!")

    def login_customer(self):
        status, customer = CustomerController.find_by_username_and_password(
            self.username_entry.value.get(),
            self.password_entry.value.get(),
        )
        if status:
            self.destroy()
            CustomerPage(customer)

        else:
            msg.showerror("login Error", "Username or Password is not correct!")

    def __init__(self, role):
        super().__init__()

        self.title("Login")
        self.geometry("300x200")
        bg_color = "light cyan"
        self.configure(bg=bg_color)

        match role.lower():
            case "admin":
                self.text = "Login Admin"
                self.command = self.login_admin
            case "employee":
                self.text = "Login Employee"
                self.command = self.login_employee
            case "customer":
                self.text = "Login Customer"
                self.command = self.login_customer

        # Label for login page
        # note: modify text part for your page
        self.label = tk.Label(self, text=self.text, bg=bg_color, font=("Arial", 20))
        self.label.place(x=20, y=10)

        # Username and Password entries
        self.username_entry = TextWithLabel(self, "Username : ", 20, 85, bg_color, 80)
        self.password_entry = TextWithLabel(self, "Password : ", 20, 115, bg_color, 80)

        # Login button
        self.login_key = tk.Button(self, bg=bg_color, text="Login", width=10, command=self.command)
        self.login_key.place(x=144, y=155)

        self.mainloop()
