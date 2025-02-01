import tkinter as tk
from tkinter import ttk
from database import UserModel
from auth_controller import AuthController
from views.login_view import LoginView
from views.signup_view import SignupView
from views.dashboard_view import DashboardView
from styles import Styles

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("سیستم مدیریت کاربران")
        self.geometry("600x400")
        self.styles = Styles()
        
        # مدل و کنترلر
        self.user_model = UserModel()
        self.auth_controller = AuthController(self.user_model)
        
        self._setup_container()
        self.show_login()

    def _setup_container(self):
        self.container = ttk.Frame(self)
        self.container.pack(fill='both', expand=True)

    def show_login(self):
        self._clear_container()
        LoginView(self.container, 
                 self.auth_controller,
                 self.show_signup).pack(fill='both', expand=True)

    def show_signup(self):
        self._clear_container()
        SignupView(self.container, 
                  self.auth_controller,
                  self.show_login).pack(fill='both', expand=True)

    def show_dashboard(self, user_data):
        self._clear_container()
        DashboardView(self.container,
                     user_data,
                     self._logout).pack(fill='both', expand=True)

    def _logout(self):
        self.auth_controller.logout()
        self.show_login()

    def _clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()