class Employee:
    """Collect name and last name and give annual salary."""
    def __init__(self, first_name, last_name, annual_salary):
        """Collect data of full name and annual salary"""
        self.first = first_name
        self.last = last_name
        self.annual_salary = annual_salary
    def give_raise(self,amount = 5000 ):
        """Give raise to salary"""
        self.annual_salary += amount

