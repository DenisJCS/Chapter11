from employee import Employee
"""Test employee program """

def test_give_default():
    employee = Employee('Chandler', 'Bing', 20000)
    employee.give_raise()
    assert employee.annual_salary == 25000 

def test_give_custom_raise():
    employee = Employee('Jouye', 'Tribiani', 23000)
    employee.give_raise(10000)
    assert employee.annual_salary == 33000
    
