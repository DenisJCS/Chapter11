from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Janis Jolpin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == "Janis Joplin"


Chapter11 % python3 -m pytest
========================================== test session starts ===========================================
platform darwin -- Python 3.12.3, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/denis_jcs/Documents/Chapter11
collected 1 item                                                                                         

test_name_function.py .                                                                            [100%]

=========================================== 1 passed in 0.00s ============================================
