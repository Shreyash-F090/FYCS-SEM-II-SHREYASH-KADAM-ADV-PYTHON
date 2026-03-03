import tkinter as tk
from database import Database
from login_page import LoginPage
from dashboard_page import DashboardPage

class AppController(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("F090 Shreyash")
        self.state('zoomed')
        self.db = Database()
        self.current_user_role = "user"

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginPage, DashboardPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == "DashboardPage":
            frame.load_data()

if __name__ == "__main__":
    AppController().mainloop()
