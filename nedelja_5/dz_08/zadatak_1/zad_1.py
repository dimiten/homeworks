from company import Company
from employee import Employee

employee1 = Employee("Dragan", "Stankovic", "3475910348531", 30, "Engineer")
employee2 = Employee("Marko", "Miladinovic", "3395739185439", 25, "Accounting")
employee3 = Employee("Jovan", "Cvetkovic", "1285643908563", 20, "Management")
employee4 = Employee("Dusan", "Ristic", "2575930485931", 15, "Track worker")
employee5 = Employee("Dejan", "Bozic", "1458372374913", 30, "Engineer")

google = Company(pib="5365626", name="Google")

google.hire_employee(employee=employee1)
google.hire_employee(employee=employee2)
google.hire_employee(employee=employee3)
google.hire_employee(employee=employee4)
google.hire_employee(employee=employee5)
