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
    
python3 -m pytest
========================================== test session starts ===========================================
platform darwin -- Python 3.12.3, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/denis_jcs/Documents/Chapter11/employee
collected 1 item                                                                                         

test_employee.py .                                                                                 [100%]

=========================================== 1 passed in 0.00s ============================================
python3 -m pytest 
========================================== test session starts ===========================================
platform darwin -- Python 3.12.3, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/denis_jcs/Documents/Chapter11/employee
collected 2 items                                                                                        

test_employee.py ..                                                                                [100%]

=========================================== 2 passed in 0.01s ============================================
