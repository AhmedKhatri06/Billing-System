import tkinter as tk
from tkinter import messagebox, ttk

class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FAUS Electronics Billing System")
        
        # Customer Details
        self.cust_name = tk.StringVar()
        self.cust_no = tk.StringVar()
        self.cust_email = tk.StringVar()
        
        # Item Details
        self.items = []
        self.total = 0
        
        # Create UI Elements
        self.create_widgets()
        
    def create_widgets(self):
        # Customer Information
        tk.Label(self.root, text="Customer Name:").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.cust_name).grid(row=0, column=1)

        tk.Label(self.root, text="Mobile Number:").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.cust_no).grid(row=1, column=1)

        tk.Label(self.root, text="Email ID:").grid(row=2, column=0)
        tk.Entry(self.root, textvariable=self.cust_email).grid(row=2, column=1)

        tk.Label(self.root, text="Number of Items:").grid(row=3, column=0)
        self.num_items_entry = tk.Entry(self.root)
        self.num_items_entry.grid(row=3, column=1)

        tk.Button(self.root, text="Add Items", command=self.add_items).grid(row=4, columnspan=2)

        # Item List
        self.tree = ttk.Treeview(self.root, columns=("Sr.no", "Item Name", "Item Code", "Price", "Quantity", "Item Total"), show='headings')
        self.tree.heading("Sr.no", text="Sr.no")
        self.tree.heading("Item Name", text="Item Name")
        self.tree.heading("Item Code", text="Item Code")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Item Total", text="Item Total")
        self.tree.grid(row=5, columnspan=2)

        tk.Button(self.root, text="Generate Bill", command=self.generate_bill).grid(row=6, columnspan=2)

    def add_items(self):
        try:
            num = int(self.num_items_entry.get())
            if num > 10:
                messagebox.showerror("Error", "You cannot add more than 10 items.")
                return
            
            for i in range(num):
                item_code = int(input("Enter Item Code: "))
                item_name = input("Enter Item Name: ")
                item_price = float(input("Enter Item Price: "))
                item_qty = int(input("Enter Item Quantity: "))
                
                item_total = item_qty * item_price
                self.total += item_total
                self.items.append((i + 1, item_name, item_code, item_price, item_qty, item_total))
                self.tree.insert("", "end", values=(i + 1, item_name, item_code, item_price, item_qty, item_total))
                
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter the correct data type.")

    def generate_bill(self):
        bill_details = f"Customer Name: {self.cust_name.get()}\n"
        bill_details += f"Customer Number: {self.cust_no.get()}\n"
        bill_details += f"Customer Email-ID: {self.cust_email.get()}\n"
        bill_details += "------Bill Summary---------\n"
        bill_details += f"{'Sr.no':<10} {'Item Name':<20} {'Item Code':<10} {'Price':<10} {'Quantity':<10} {'Item Total':<10}\n"
        
        for item in self.items:
            bill_details += f"{item[0]:<10} {item[1]:<20} {item[2]:<10} {item[3]:<10} {item[4]:<10} {item[5]:<10}\n"
        
        bill_details += f"\nTotal Amount = {self.total:.2f}"
        messagebox.showinfo("Bill Summary", bill_details)

if __name__ == "__main__":
    root = tk.Tk()
    app = BillingApp(root)
    root.mainloop()
