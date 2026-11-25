# Employee_Mangment_System

Employee Management System

A simple desktop-based Employee Management System developed using Python, Tkinter, and MySQL. This application allows users to manage employee records through a graphical user interface (GUI).

The project demonstrates Python programming, database connectivity, and CRUD operations using MySQL.

Features

- Add Employee: Add new employee records with details such as name, salary, department, age, and gender.
- View Employees: Display all employee records in a table.
- Update Employee: Modify the details of an existing employee.
- Delete Employee: Remove employee records from the database.
- Clear Fields: Clear the input fields.
- Refresh Records: Reload employee records from the database.
- Input Validation: Validate employee details before saving them.

Technologies Used

- Python
- Tkinter – For the graphical user interface
- MySQL – For database management
- MySQL Connector/Python – For connecting Python with MySQL

Project Structure

Emp_management/
│
├── app.py          # Main application and GUI
├── database.py     # Database connection and CRUD operations
└── README.md       # Project documentation

Requirements

Before running the application, make sure you have:

- Python 3.x installed
- MySQL Server installed and running
- MySQL Workbench (optional, for database management)

Installation and Setup

1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git

Navigate to the project directory:

cd YOUR_REPOSITORY_NAME

2. Install Required Python Package

Install the MySQL Connector:

pip install mysql-connector-python

Tkinter is generally included with standard Python installations.

3. Configure MySQL Connection

Open "database.py" and update the database connection settings according to your MySQL configuration.

DB_CONFIG = {
    'host': '127.0.0.1',
    'port': '3306',
    'user': 'root',
    'password': 'YOUR_MYSQL_PASSWORD',
    'use_pure': True
}

Replace "YOUR_MYSQL_PASSWORD" with your MySQL password.

Note: The application automatically creates the "employee_management" database and the "employees" table if they do not already exist.

4. Run the Application

Execute the following command:

python app.py

The Employee Management System window will open, allowing you to manage employee records.

Database Structure

Database Name: "employee_management"

Table Name: "employees"

Column Name| Data Type| Description
employee_id| INT| Unique employee ID (Primary Key, Auto Increment)
employee_name| VARCHAR(50)| Employee name
salary| DECIMAL(10,2)| Employee salary
department| VARCHAR(100)| Employee department
age| INT| Employee age
gender| VARCHAR(10)| Employee gender

CRUD Operations

The application supports the following database operations:

Operation| Description
Create| Insert new employee records
Read| Retrieve and display employee records
Update| Modify existing employee records
Delete| Remove employee records

Learning Outcomes

Through this project, I gained practical experience in:

- Developing desktop applications using Python and Tkinter.
- Connecting Python applications with MySQL databases.
- Implementing CRUD operations using SQL.
- Handling database connections and transactions.
- Validating user input and handling exceptions.
- Building a graphical user interface for database management.

Future Improvements

- Add employee search functionality.
- Improve the user interface design.
- Add login and authentication functionality.
- Generate employee reports.
- Add salary and department-based filtering.

Author

Ritik Paliwal

Aspiring Data Analyst | Python | SQL | Excel

"GitHub Profile" (https://github.com/ritik-paliwal)
