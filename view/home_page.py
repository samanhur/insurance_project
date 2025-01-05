import tkinter as tk


class HomePage(tk.Tk):
    def sign_up(self):
        print("sign up")

    def login(self):
        print("login")

    def personnel(self):
        print("personnel")

    def products(self):
        print("products")

    def __init__(self):
        super().__init__()

        self.title("Home page")
        self.geometry("500x300")
        bg_color = "light cyan"

        # Main page frame
        self.main_frame = tk.Frame(self, bg=bg_color, highlightbackground="black", highlightthickness=1, width=500,
                                   height=300)
        self.main_frame.place(x=0, y=0)

        # Frame for buttons
        self.button_frame = tk.Frame(self, bg=bg_color, highlightbackground="black", highlightthickness=1, width=500,
                                     height=37)
        self.button_frame.place(x=0, y=0)

        # Entering users buttons
        self.sign_up_button = tk.Button(self, bg=bg_color, text="Sing Up", width=10, command=self.sign_up)
        self.sign_up_button.place(x=5, y=5)

        self.login_button = tk.Button(self, bg=bg_color, text="Login", width=10, command=self.login)
        self.login_button.place(x=94, y=5)

        # Entering personnel button
        self.personnel_button = tk.Button(self, bg=bg_color, text="Personnel", width=10, command=self.personnel)
        self.personnel_button.place(x=412, y=5)

        # Insurance Label and description
        tk.Label(self, text="Insurance", bg=bg_color, font=("Arial", 25)).place(x=180, y=85)
        # todo:
        description = "some description about company"
        tk.Label(self, text=description, bg=bg_color, font=("Arial", 10)).place(x=160, y=160)

        # Product button for showing insurances list
        self.product_button = tk.Button(self, text="Products", bg=bg_color, width=15, font=("Arial", 18),
                                        command=self.products)
        self.product_button.place(x=148, y=230)

        self.mainloop()


page = HomePage()
