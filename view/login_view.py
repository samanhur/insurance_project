import tkinter as tk

from view.components import TextWithLabel


class LoginPage(tk.Tk):
    def login_admin(self):
        # self.destroy()
        print("login admin")

    def login_employee(self):
        print("login employee")

    def login_customer(self):
        print("login customer")

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
        self.username_entry = TextWithLabel(self, "Username : ", 20, 85, bg_color)
        self.password_entry = TextWithLabel(self, "Password : ", 20, 115, bg_color)

        # Login button
        self.login_key = tk.Button(self, bg=bg_color, text="Login", width=10, command=self.command)
        self.login_key.place(x=144, y=155)

        self.mainloop()

# login_page = LoginPage("Login customer")
