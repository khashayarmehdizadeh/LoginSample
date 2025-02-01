import tkinter as tk
from tkinter import ttk, messagebox
from styles import Styles

class LoginView(tk.Frame):
    def __init__(self, parent, controller, switch_to_signup):
        super().__init__(parent)
        self.controller = controller
        self.styles = Styles()
        self._setup_ui(switch_to_signup)

    def _setup_ui(self, switch_to_signup):
        self.configure(style=self.styles.main_frame)
        
        # عنوان
        ttk.Label(self, text="ورود به سیستم", style='Header.TLabel').pack(pady=20)

        # فرم ورود
        form_frame = ttk.Frame(self, style='Secondary.TFrame')
        form_frame.pack(pady=10, padx=20, fill='x')

        ttk.Label(form_frame, text="نام کاربری:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.username_entry = ttk.Entry(form_frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

        ttk.Label(form_frame, text="رمز عبور:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.password_entry = ttk.Entry(form_frame, show='*')
        self.password_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

        # دکمه‌ها
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=20)

        ttk.Button(btn_frame, text="ورود", command=self._login, style='Primary.TButton').pack(side='left', padx=5)
        ttk.Button(btn_frame, text="ثبت نام", command=switch_to_signup).pack(side='left', padx=5)

    def _login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        result = self.controller.login(username, password)
        if result['success']:
            self._clear_form()
            messagebox.showinfo("موفق", f"خوش آمدید {username}!")
            self.master.show_dashboard(result['user'])
        else:
            messagebox.showerror("خطا", result['error'])

    def _clear_form(self):
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')