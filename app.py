# app.py
# Simple Employee Management System using Tkinter + MySQL.

import tkinter as tk
from tkinter import ttk, messagebox
import database


def clear_fields():
    selected_id.set("")
    name_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)
    department_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_combo.set("")


def get_form_data():
    name = name_entry.get().strip()
    salary = salary_entry.get().strip()
    department = department_entry.get().strip()
    age = age_entry.get().strip()
    gender = gender_combo.get().strip()

    if not all([name, salary, department, age, gender]):
        raise ValueError("Please fill in all fields.")

    try:
        salary = float(salary)
        age = int(age)
        if salary < 0 or age <= 0:
            raise ValueError
    except ValueError:
        raise ValueError("Salary must be a positive number and age must be a positive whole number.")

    return name, salary, department, age, gender


def load_employees():
    for item in employee_table.get_children():
        employee_table.delete(item)

    try:
        for employee in database.get_all_employees():
            employee_table.insert("", tk.END, values=employee)
    except Exception as error:
        messagebox.showerror("Database Error", str(error))


def add_employee():
    try:
        data = get_form_data()
        database.insert_employee(*data)
        messagebox.showinfo("Success", "Employee added successfully.")
        clear_fields()
        load_employees()
    except ValueError as error:
        messagebox.showwarning("Input Error", str(error))
    except Exception as error:
        messagebox.showerror("Error", str(error))


def update_employee():
    if not selected_id.get():
        messagebox.showwarning("Select Employee", "Select an employee from the table first.")
        return

    try:
        data = get_form_data()
        changed = database.update_employee(int(selected_id.get()), *data)
        if changed:
            messagebox.showinfo("Success", "Employee updated successfully.")
        else:
            messagebox.showinfo("Information", "No changes were made.")
        clear_fields()
        load_employees()
    except ValueError as error:
        messagebox.showwarning("Input Error", str(error))
    except Exception as error:
        messagebox.showerror("Error", str(error))


def delete_employee():
    if not selected_id.get():
        messagebox.showwarning("Select Employee", "Select an employee from the table first.")
        return

    if not messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this employee?"):
        return

    try:
        deleted = database.delete_employee(int(selected_id.get()))
        if deleted:
            messagebox.showinfo("Success", "Employee deleted successfully.")
        else:
            messagebox.showinfo("Information", "Employee not found.")
        clear_fields()
        load_employees()
    except Exception as error:
        messagebox.showerror("Error", str(error))


def select_employee(event):
    selected = employee_table.focus()
    if not selected:
        return

    values = employee_table.item(selected, "values")
    if values:
        selected_id.set(values[0])

        clear_visible_fields()
        name_entry.insert(0, values[1])
        salary_entry.insert(0, values[2])
        department_entry.insert(0, values[3])
        age_entry.insert(0, values[4])
        gender_combo.set(values[5])


def clear_visible_fields():
    name_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)
    department_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_combo.set("")


# -------------------- WINDOW --------------------

root = tk.Tk()
root.title("Employee Management System")
root.geometry("900x600")
root.resizable(False, False)

selected_id = tk.StringVar()

heading = tk.Label(root, text="Employee Management System",
                   font=("Arial", 20, "bold"))
heading.pack(pady=12)

form_frame = tk.LabelFrame(root, text="Employee Details", padx=12, pady=10)
form_frame.pack(fill="x", padx=20, pady=5)

tk.Label(form_frame, text="Employee Name").grid(row=0, column=0, sticky="w", padx=5, pady=5)
name_entry = tk.Entry(form_frame, width=25)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Salary").grid(row=0, column=2, sticky="w", padx=5, pady=5)
salary_entry = tk.Entry(form_frame, width=25)
salary_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Label(form_frame, text="Department").grid(row=1, column=0, sticky="w", padx=5, pady=5)
department_entry = tk.Entry(form_frame, width=25)
department_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Age").grid(row=1, column=2, sticky="w", padx=5, pady=5)
age_entry = tk.Entry(form_frame, width=25)
age_entry.grid(row=1, column=3, padx=5, pady=5)

tk.Label(form_frame, text="Gender").grid(row=2, column=0, sticky="w", padx=5, pady=5)
gender_combo = ttk.Combobox(form_frame, values=["Male", "Female", "Other"],
                            state="readonly", width=22)
gender_combo.grid(row=2, column=1, padx=5, pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Employee", width=15, command=add_employee).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Update Employee", width=15, command=update_employee).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete Employee", width=15, command=delete_employee).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Clear", width=12, command=clear_fields).grid(row=0, column=3, padx=5)
tk.Button(button_frame, text="Refresh", width=12, command=load_employees).grid(row=0, column=4, padx=5)

table_frame = tk.Frame(root)
table_frame.pack(fill="both", expand=True, padx=20, pady=10)

columns = ("ID", "Name", "Salary", "Department", "Age", "Gender")
employee_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=13)

for column in columns:
    employee_table.heading(column, text=column)
    employee_table.column(column, width=135, anchor="center")

employee_table.pack(fill="both", expand=True)
employee_table.bind("<<TreeviewSelect>>", select_employee)

# Create the database/table and show existing employees.
try:
    database.get_connection().close()
    load_employees()
except Exception as error:
    messagebox.showerror(
        "MySQL Connection Error",
        "Could not connect to MySQL.\n\n"
        "1. Check that the MySQL server is running.\n"
        "2. Check the password in database.py.\n"
        "3. Install mysql-connector-python.\n\n"
        f"Details: {error}"
    )

root.mainloop()
