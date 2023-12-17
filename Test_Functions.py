from functions import salary, hello_who

def test_hello_who_max():
    assert hello_who('max') == 'Hello, max'
    assert hello_who('govnoedus') == 'Hello, govnoedus'
    assert hello_who('vladbik') == 'Hello, vladbik'
    assert hello_who('chert') == 'Hello, chert'

def test_salary():
    assert(2, 2) != 8
    assert(3, 1) !=     6