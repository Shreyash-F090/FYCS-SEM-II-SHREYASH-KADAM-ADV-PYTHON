import tkinter as tk
from tkinter import messagebox

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#2c3e50")
        self.controller = controller
        
        self.controller.bind('<Return>', lambda e: self.do_login())
        
        card = tk.Frame(self, bg="white", padx=50, pady=50)
        card.place(relx=0.5, rely=0.5, anchor="center")
        
        tk.Label(card, text="SYSTEM LOGIN", font=("Arial", 22, "bold"), bg="white").pack(pady=20)
        
        tk.Label(card, text="Username", bg="white", fg="grey").pack(anchor="w")
        self.u_ent = tk.Entry(card, font=("Arial", 14), bg="#f5f6fa", width=30)
        self.u_ent.pack(pady=5)
        
        tk.Label(card, text="Password", bg="white", fg="grey").pack(anchor="w")
        self.p_ent = tk.Entry(card, show="*", font=("Arial", 14), bg="#f5f6fa", width=30)
        self.p_ent.pack(pady=5)
        
        tk.Button(card, text="LOGIN", bg="#3498db", fg="white", font=("Arial", 12, "bold"), 
                  command=self.do_login, width=25).pack(pady=20, ipady=5)

    def do_login(self):
        res = self.controller.db.authenticate(self.u_ent.get(), self.p_ent.get())
        if res:
            self.controller.current_user_role = res[0]
            self.controller.show_frame("DashboardPage")
        else:
            messagebox.showerror("Error", "Invalid Username or Password")
