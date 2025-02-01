import tkinter as tk
from tkinter import ttk
from styles import Styles

class DashboardView(tk.Frame):
    def __init__(self, parent, user_data, logout_callback):
        super().__init__(parent)
        self.styles = Styles()
        self.logout_callback = logout_callback
        self._setup_ui(user_data)

    def _setup_ui(self, user_data):
        self.configure(style=self.styles.main_frame)
        
        # عنوان
        ttk.Label(self, 
                 text=f"پنل کاربری {user_data[0]}",
                 style='Header.TLabel').pack(pady=20)

        # اطلاعات کاربر
        info_frame = ttk.LabelFrame(self, text=" اطلاعات حساب ", style='Secondary.TFrame')
        info_frame.pack(pady=10, padx=20, fill='both', expand=True)

        ttk.Label(info_frame, text="نام کاربری:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        ttk.Label(info_frame, text=user_data[0]).grid(row=0, column=1, padx=10, pady=5, sticky='w')

        ttk.Label(info_frame, text="ایمیل:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        ttk.Label(info_frame, text=user_data[1] or '-').grid(row=1, column=1, padx=10, pady=5, sticky='w')

        ttk.Label(info_frame, text="تاریخ عضویت:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
        ttk.Label(info_frame, text=user_data[2]).grid(row=2, column=1, padx=10, pady=5, sticky='w')

        # دکمه خروج
        ttk.Button(self, 
                  text="خروج از سیستم",
                  command=self.logout_callback,
                  style='Danger.TButton').pack(pady=20)
