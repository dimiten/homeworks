"""Model for describing companies."""

import typing as t
from employee import Employee
from employee_datetime import MONTHS_PER_YEAR


class Company:
    """Model for company."""

    def __init__(self, pib: str, name: str, employees: t.List[Employee] = []):
        """Initialize the Company object."""
        self.pib = pib
        self.name = name
        self.employees = employees

    def find_employee_by_jmbg(self, jmbg: str):
        """Find employee by jmbg if exists in list of employees."""
        for e in self.employees:
            if e.jmbg == jmbg:
                return e

        return None

    def hire_employee(self, employee: Employee):
        """Hire an employee."""
        if self.find_employee_by_jmbg(jmbg=employee.jmbg) is not None:
            raise Exception("We already have that employee employed!")

        self.employees.append(employee)

    def fire_employee(self, employee: Employee):
        """Fire an empolyee."""
        if self.find_employee_by_jmbg(jmbg=employee.jmbg) is None:
            raise Exception("We don't have that employee employed!")

        self.employees.remove(employee)

    def calculate_monthly_salaries_for_all(self):
        """Calculates how much money the company pays her employees per month"""
        monthly_salaries_for_all = 0
        for e in self.employees:
            monthly_salaries_for_all += e.calculate_monthly_income()

        return monthly_salaries_for_all

    def calculate_annual_salaries_for_all(self):
        """Calculates how much money the company pays her employees per year"""
        return self.calculate_monthly_salaries_for_all() * MONTHS_PER_YEAR

    def all_positions_in_company(self):
        """Returns a list of all positions in the company"""
        list_of_postions = []
        for e in self.employees:
            if e.position not in list_of_postions:
                list_of_postions.append(e.position)

        return list_of_postions

    def calculate_monthly_salaries_for_position(self, position: str):
        """Calculates how much money the company pays for a position per month"""
        monthly_salaries_for_position = 0
        for e in self.employees:
            if e.position == position:
                monthly_salaries_for_position += e.calculate_monthly_income()

        return monthly_salaries_for_position

    def calculate_annual_salaries_for_position(self, position: str):
        """Calculates how much money the company pays for a position per year"""
        return self.calculate_monthly_salaries_for_position(position=position) * MONTHS_PER_YEAR
