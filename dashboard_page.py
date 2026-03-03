import tkinter as tk
from tkinter import ttk, messagebox

class DashboardPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f8f9fa")
        self.controller = controller

        # --- SIDEBAR ---
        sidebar = tk.Frame(self, bg="#2c3e50", width=220)
        sidebar.pack(side="left", fill="y")
        
        tk.Label(sidebar, text="Shreyash electronic shop", font=("Impact", 28), bg="#2c3e50", fg="#3498db").pack(pady=40)
        
        tk.Button(sidebar, text="LOGOUT", font=("Arial", 10, "bold"), bg="#e74c3c", fg="white", 
                  relief="flat", cursor="hand2", command=lambda: controller.show_frame("LoginPage")).pack(side="bottom", fill="x", padx=20, pady=30)

        # --- MAIN CONTAINER ---
        main_view = tk.Frame(self, bg="#f8f9fa")
        main_view.pack(side="right", fill="both", expand=True)

        # --- GLOBAL HEADER ---
        header = tk.Frame(main_view, bg="white", height=70, bd=1, relief="flat")
        header.pack(fill="x", padx=20, pady=20)
        
        tk.Label(header, text="🔍", bg="white", font=("Arial", 12)).pack(side="left", padx=(20, 5))
        self.search_ent = tk.Entry(header, width=35, font=("Arial", 11), bg="#f1f3f4", relief="flat")
        self.search_ent.pack(side="left", padx=5, ipady=6)
        self.search_ent.bind('<Return>', lambda e: self.load_data())

        self.rev_lbl = tk.Label(header, text="REVENUE: ₹0.00", font=("Segoe UI", 16, "bold"), 
                                bg="white", fg="#27ae60")
        self.rev_lbl.pack(side="right", padx=30)

        # --- DATA TABLE WITH SCROLLBAR ---
        table_container = tk.Frame(main_view, bg="white", padx=15, pady=15)
        table_container.pack(fill="both", expand=True, padx=20)

        # 1. Create Scrollbar
        tree_scroll = tk.Scrollbar(table_container)
        tree_scroll.pack(side="right", fill="y")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", rowheight=35, font=("Arial", 10), background="white", fieldbackground="white")
        style.configure("Treeview.Heading", font=("Arial", 11, "bold"), background="#f8f9fa", relief="flat")
        style.map("Treeview", background=[('selected', '#3498db')])

        # 2. Link Scrollbar to Treeview
        self.tree = ttk.Treeview(table_container, columns=("ID", "Name", "Price", "Stock"), 
                                 show="headings", yscrollcommand=tree_scroll.set)
        
        tree_scroll.config(command=self.tree.yview)

        for col in ("ID", "Name", "Price", "Stock"):
            self.tree.heading(col, text=col.upper())
            self.tree.column(col, anchor="center", width=100)
        self.tree.pack(fill="both", expand=True)

        # --- ACTION PANEL GRID ---
        actions_grid = tk.Frame(main_view, bg="#f8f9fa")
        actions_grid.pack(fill="x", padx=15, pady=20)
        actions_grid.columnconfigure((0, 1, 2, 3), weight=1)

        def create_card(title, color):
            frame = tk.LabelFrame(actions_grid, text=f" {title} ", bg="white", 
                                  font=("Arial", 10, "bold"), fg=color, padx=10, pady=10)
            return frame

        # Cards... (Keep your existing card definitions for Sales, Restock, New Item here)
        s_card = create_card("Sales", "#2980b9")
        s_card.grid(row=0, column=0, padx=8, sticky="nsew")
        tk.Label(s_card, text="Product ID", bg="white").pack(); self.s_id = tk.Entry(s_card, bg="#f8f9fa"); self.s_id.pack(pady=2)
        tk.Label(s_card, text="Quantity", bg="white").pack(); self.s_qty = tk.Entry(s_card, bg="#f8f9fa"); self.s_qty.pack(pady=2)
        tk.Button(s_card, text="COMPLETE SALE", bg="#2980b9", fg="white", relief="flat", command=self.handle_sale).pack(pady=10, fill="x")

        r_card = create_card("Restock Product", "#27ae60")
        r_card.grid(row=0, column=1, padx=8, sticky="nsew")
        tk.Label(r_card, text="Product ID", bg="white").pack(); self.r_id = tk.Entry(r_card, bg="#f8f9fa"); self.r_id.pack(pady=2)
        tk.Label(r_card, text="Add Amount", bg="white").pack(); self.r_qty = tk.Entry(r_card, bg="#f8f9fa"); self.r_qty.pack(pady=2)
        tk.Button(r_card, text="UPDATE STOCK", bg="#27ae60", fg="white", relief="flat", command=self.handle_restock).pack(pady=10, fill="x")

        n_card = create_card("New Product", "#8e44ad")
        n_card.grid(row=0, column=2, padx=8, sticky="nsew")
        tk.Label(n_card, text="Name", bg="white").pack(); self.n_name = tk.Entry(n_card, bg="#f8f9fa"); self.n_name.pack(pady=1)
        tk.Label(n_card, text="Price", bg="white").pack(); self.n_price = tk.Entry(n_card, bg="#f8f9fa"); self.n_price.pack(pady=1)
        tk.Label(n_card, text="Stock", bg="white").pack(); self.n_stock = tk.Entry(n_card, bg="#f8f9fa"); self.n_stock.pack(pady=1)
        self.add_btn = tk.Button(n_card, text="ADD TO SYSTEM", bg="#8e44ad", fg="white", relief="flat", command=self.handle_new)
        self.add_btn.pack(pady=10, fill="x")

        d_card = create_card("Delete Product", "#c0392b")
        d_card.grid(row=0, column=3, padx=8, sticky="nsew")
        tk.Label(d_card, text="Product ID", bg="white").pack()
        self.d_id = tk.Entry(d_card, bg="#f8f9fa"); self.d_id.pack(pady=5)
        self.del_btn = tk.Button(d_card, text="DELETE PERMANENTLY", bg="#c0392b", fg="white", relief="flat", command=self.handle_delete)
        self.del_btn.pack(pady=10, fill="x")

    # --- LOGIC ---
    def load_data(self):
        role = self.controller.current_user_role
        self.add_btn.config(state="normal" if role == "admin" else "disabled")
        self.del_btn.config(state="normal" if role == "admin" else "disabled")

        for i in self.tree.get_children(): self.tree.delete(i)
        for row in self.controller.db.get_products(self.search_ent.get()):
            self.tree.insert("", "end", values=row)
        self.rev_lbl.config(text=f"REVENUE: ₹{self.controller.db.get_revenue():.2f}")

    def handle_sale(self):
        try:
            if self.controller.db.process_sale(int(self.s_id.get()), int(self.s_qty.get())):
                self.load_data()
                messagebox.showinfo("Success", "Transaction Complete")
            else: messagebox.showwarning("Stock", "Insufficient stock available")
        except: messagebox.showerror("Error", "Invalid Input")

    def handle_restock(self):
        try:
            self.controller.db.update_stock(int(self.r_id.get()), int(self.r_qty.get()))
            self.load_data()
        except: messagebox.showerror("Error", "Invalid ID or Amount")

    def handle_new(self):
        try:
            self.controller.db.add_product(self.n_name.get(), float(self.n_price.get()), int(self.n_stock.get()))
            self.load_data()
            self.n_name.delete(0, tk.END)
            self.n_price.delete(0, tk.END)
            self.n_stock.delete(0, tk.END)
        except: messagebox.showerror("Error", "Check your inputs")

    def handle_delete(self):
        target_id = self.d_id.get()
        if not target_id:
            messagebox.showwarning("Input Error", "Enter Product ID to delete.")
            return

        if messagebox.askyesno("Confirm", f"Delete Product ID {target_id}?"):
            self.controller.db.delete_product(target_id)
            self.d_id.delete(0, tk.END) # Clear field
            self.load_data() # Force UI refresh
            messagebox.showinfo("Success", "Product removed from database.")
