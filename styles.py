from tkinter import ttk

class Styles:
    def __init__(self):
        self._configure_styles()

    def _configure_styles(self):
        style = ttk.Style()
        
        # رنگ‌های اصلی
        style.theme_create('custom', parent='alt', settings={
            'TFrame': {'configure': {'background': '#f0f2f5'}},
            
            'Header.TLabel': {
                'configure': {
                    'font': ('Helvetica', 16, 'bold'),
                    'foreground': '#2d3436',
                    'background': '#f0f2f5'
                }
            },
            
            'Primary.TButton': {
                'configure': {
                    'background': '#1877f2',
                    'foreground': 'white',
                    'font': ('Helvetica', 10, 'bold'),
                    'padding': 8
                },
                'map': {
                    'background': [('active', '#166fe5')]
                }
            },
            
            'Danger.TButton': {
                'configure': {
                    'background': '#dc3545',
                    'foreground': 'white'
                }
            },
            
            'Secondary.TFrame': {
                'configure': {
                    'background': 'white',
                    'relief': 'groove',
                    'borderwidth': 2
                }
            }
        })
        style.theme_use('custom')