import tkinter as tk

from view.login_view import LoginPage


class Personnel(tk.Tk):

    def employee(self):
        self.destroy()
        LoginPage("employee")
        print("employee")

    def admin(self):
        self.destroy()
        LoginPage("admin")
        print("admin")

    def __init__(self):
        super().__init__()

        self.title("Personnel")
        self.geometry("200x150")
        bg_color = "light cyan"
        self.configure(bg=bg_color)

        # Employee Button
        self.employee_button = tk.Button(self, bg=bg_color, text="Employee", width=10, command=self.employee)
        self.employee_button.place(x=60, y=30)
        # Admin Button
        self.admin_button = tk.Button(self, bg=bg_color, text="Admin", width=10, command=self.admin)
        self.admin_button.place(x=60, y=80)

        self.mainloop()


