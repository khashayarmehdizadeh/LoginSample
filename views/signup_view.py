import tkinter as tk
from tkinter import ttk, messagebox
from styles import Styles

class SignupView(tk.Frame):
    def __init__(self, parent, controller, switch_to_login):
        super().__init__(parent)
        self.controller = controller
        self.styles = Styles()
        self._setup_ui(switch_to_login)

    def _setup_ui(self, switch_to_login):
        self.configure(style=self.styles.main_frame)
        
        # عنوان
        ttk.Label(self, text="ثبت نام", style='Header.TLabel').pack(pady=20)

        # فرم ثبت نام
        form_frame = ttk.Frame(self, style='Secondary.TFrame')
        form_frame.pack(pady=10, padx=20, fill='x')

        ttk.Label(form_frame, text="نام کاربری:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.username_entry = ttk.Entry(form_frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

        ttk.Label(form_frame, text="رمز عبور:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.password_entry = ttk.Entry(form_frame, show='*')
        self.password_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

        ttk.Label(form_frame, text="تکرار رمز عبور:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.confirm_password_entry = ttk.Entry(form_frame, show='*')
        self.confirm_password_entry.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

        # دکمه‌ها
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=20)

        ttk.Button(btn_frame, text="ثبت نام", command=self._signup, style='Primary.TButton').pack(side='left', padx=5)
        ttk.Button(btn_frame, text="بازگشت به ورود", command=switch_to_login).pack(side='left', padx=5)

    def _signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            messagebox.showerror("خطا", "رمز عبور و تکرار رمز عبور مطابقت ندارند.")
            return

        result = self.controller.signup(username, password)
        if result['success']:
            self._clear_form()
            messagebox.showinfo("موفق", f"ثبت نام با موفقیت انجام شد {username}!")
            self.master.show_login()
        else:
            messagebox.showerror("خطا", result['error'])

    def _clear_form(self):
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        self.confirm_password_entry.delete(0, 'end')