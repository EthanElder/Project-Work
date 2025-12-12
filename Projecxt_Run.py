import tkinter as tk
from tkinter import messagebox

global entry

customerDictionary = {}
employeeDictionary = {}
productList = []

class Customer:
    def add_customer(self, user_id, username, pword):
        customerDictionary[username] = {"user_id": user_id, "pword": pword}

    def customer_login(self, username, pword):
        if username in customerDictionary:
            if customerDictionary[username]["pword"] == pword:
                return True
        return False


class Employee:
    def add_employee(self, emp_id, emp_name, password, position, rate):
        employeeDictionary[emp_id] = {
            "employee_name": emp_name,
            "employee_password": password,
            "position": position,
            "rate": rate
        }

    def employee_login(self, emp_id, password):
        if emp_id in employeeDictionary:
            if employeeDictionary[emp_id]["employee_password"] == password:
                return True
        return False


class Login_App:
    def __init__(self, root):
        self.customer = Customer()
        self.employee = Employee()
        self.root = root
        self.root.title("Login System")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        tk.Label(root, text="User ID / Username:").pack(pady=5)
        self.entry_user = tk.Entry(root, width=30)
        self.entry_user.pack(pady=5)

        tk.Label(root, text="Password:").pack(pady=5)
        self.entry_pass = tk.Entry(root, width=30, show="*")
        self.entry_pass.pack(pady=5)

        tk.Button(root, text="Customer Login", command=self.customer_login).pack(pady=5)
        tk.Button(root, text="Employee Login", command=self.employee_login).pack(pady=5)
        tk.Button(root, text="New Customer", command=self.add_customer).pack(pady=5)
        tk.Button(root, text="New Employee", command=self.add_employee).pack(pady=5)

    def add_customer(self):
        user_id = self.entry_user.get()
        username = self.entry_user.get()
        pword = self.entry_pass.get()
        if user_id and username and pword:
            self.customer.add_customer(user_id, username, pword)
            messagebox.showinfo("Success", f"Customer '{username}' added successfully.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def add_employee(self):
        emp_id = self.entry_user.get()
        password = self.entry_pass.get()
        emp_name = emp_id
        position = "Employee"
        rate = 15.00
        if emp_id and password:
            self.employee.add_employee(emp_id, emp_name, password, position, rate)
            messagebox.showinfo("Success", f"Employee '{emp_id}' added successfully.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def customer_login(self):
        username = self.entry_user.get()
        pword = self.entry_pass.get()
        if self.customer.customer_login(username, pword):
            messagebox.showinfo("Login", "Customer login successful.")
            self.open_inventory_window("Customer")
        else:
            messagebox.showerror("Login Failed", "Invalid customer credentials.")

    def employee_login(self):
        emp_id = self.entry_user.get()
        password = self.entry_pass.get()
        if self.employee.employee_login(emp_id, password):
            messagebox.showinfo("Login", "Employee login successful.")
            self.open_inventory_window("Employee")
        else:
            messagebox.showerror("Login Failed", "Invalid employee credentials.")

    def open_inventory_window(self, role):
        inv_win = tk.Toplevel(self.root)
        inv_win.title(f"{role} Inventory")
        inv_win.geometry("400x300")

        tk.Label(inv_win, text=f"Welcome {role}!").pack(pady=20)

        tk.Label(inv_win, text="Product Name:").pack(pady=5)
        entry = tk.Entry(inv_win, width=30)
        entry.pack(pady=10)

        def add_product():
            product = entry.get().strip()
            if not product:
                messagebox.showwarning("Error", "Please enter a product name.")
                return

            productList.append(product)
            messagebox.showinfo("Inventory", f"{product} added.")
            entry.delete(0, tk.END)

        def view_cart():
            if productList:
                messagebox.showinfo("Inventory", "Products: " + ", ".join(productList))
            else:
                messagebox.showinfo("Inventory", "No products yet.")

        tk.Button(inv_win, text="Add Product", command=add_product).pack(pady=5)
        tk.Button(inv_win, text="View Cart", command=view_cart).pack(pady=5)
        tk.Button(inv_win, text="Logout", command=inv_win.destroy).pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = Login_App(root)
    root.mainloop()