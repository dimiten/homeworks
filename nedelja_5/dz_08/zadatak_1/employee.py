"""Model for Employee."""

from employee_datetime import HOURS_PER_DAY, DAYS_PER_MONTH, MONTHS_PER_YEAR


class Employee:
    """Model of instance Employee."""

    def __init__(self, name: str, surname: str, jmbg: str, hourly: int, position: str):
        """Initialize the Employee object."""
        self.name = name
        self.surname = surname
        self.jmbg = jmbg
        self.hourly = hourly
        self.position = position

    def calculate_monthly_income(self):
        """Calculate monthly income for given employee."""
        return self.hourly * HOURS_PER_DAY * DAYS_PER_MONTH

    def calculate_annual_income(self):
        """Calculate annual income for given employee."""
        return self.calculate_monthly_income() * MONTHS_PER_YEAR

    def raise_hourly_for_employee(self, raise_percent: int):
        """Raises hourly income for an employee"""
        self.hourly = self.hourly + self.hourly * (raise_percent / 100)

    def reduce_hourly_for_employee(self, reduce_percent: int):
        """Reduces hourly income for an employee"""
        self.hourly = self.hourly - self.hourly * (reduce_percent / 100)
