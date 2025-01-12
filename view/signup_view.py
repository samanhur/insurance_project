import tkinter as tk
import tkinter.messagebox as msg

from controller.customer_controller import CustomerController
from model.entity.customer import Customer
from view.components.components import TextWithLabel
from view.customer_view import CustomerPage


class SignupPage(tk.Tk):
    def signup(self):
        match self.window.lower():
            case "customer":
                if self.password.value.get() == self.confirm_password.value.get():
                    status, message = CustomerController.save(
                        self.name.value.get(),
                        self.family.value.get(),
                        self.father_name.value.get(),
                        self.national_code.value.get(),
                        self.birth_date.value.get(),
                        self.phone.value.get(),
                        self.username.value.get(),
                        self.password.value.get()
                    )
                    if status:
                        msg.showinfo("Customer Saved", "You Singed up!")
                        customer_info = Customer(self.name.value.get(),
                                                 self.family.value.get(),
                                                 self.father_name.value.get(),
                                                 self.national_code.value.get(),
                                                 self.birth_date.value.get(),
                                                 self.phone.value.get(),
                                                 self.username.value.get(),
                                                 self.password.value.get(), 1)
                        CustomerPage(customer_info=customer_info)
                        self.destroy()
                    else:
                        msg.showerror("Save Error", message)
                else:
                    raise ValueError("Password is not same!")

            case "employee":
                pass
            case "admin":
                pass

    def __init__(self, window):
        super().__init__()

        self.geometry("285x500")
        self.window = window
        self.title("Sign Up " + window.title())
        bg_color = "light cyan"
        self.configure(bg=bg_color)

        label_text = "Please enter your information:"
        self.label = tk.Label(self, text=label_text, font=("Arial", 10), bg=bg_color)
        self.label.place(x=20, y=20)

        self.name = TextWithLabel(self, "Name:", 20, 60, bg_color, 120)
        self.family = TextWithLabel(self, "Family:", 20, 100, bg_color, 120)
        self.father_name = TextWithLabel(self, "Father name:", 20, 140, bg_color, 120)
        self.national_code = TextWithLabel(self, "National code:", 20, 180, bg_color, 120)
        self.birth_date = TextWithLabel(self, "Birth date:", 20, 220, bg_color, 120)
        self.phone = TextWithLabel(self, "Phone:", 20, 260, bg_color, 120)
        self.username = TextWithLabel(self, "Username:", 20, 300, bg_color, 120)
        self.password = TextWithLabel(self, "Password:", 20, 340, bg_color, 120)
        self.confirm_password = TextWithLabel(self, "Confirm password:", 20, 380, bg_color, 120)

        self.signup_button = tk.Button(self, text="Sign Up", width=34, bg=bg_color, command=self.signup)
        self.signup_button.place(x=20, y=440)

        self.mainloop()

# page = SignupPage("Customer")
