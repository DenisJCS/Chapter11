from city_function import get_formatted_info

def test_city_country():
    "City name and it's country"
    formatted_info = get_formatted_info('Santiago', 'chile')
    assert formatted_info == "Santiago Chile"
    
def test_city_population_country():
    """City, population and country"""
    formatted_info = get_formatted_info('santiago', 'chile',  population=5000000)
    assert formatted_info == "Santiago 5000000 Chile"

11-1test % python3 -m pytest
========================================== test session starts ===========================================
platform darwin -- Python 3.12.3, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/denis_jcs/Documents/Chapter11/11-1test
collected 2 items                                                                                        

test_cities.py ..                                                                                  [100%]

=========================================== 2 passed in 0.00s ============================================
