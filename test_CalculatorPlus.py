from CalculatorPlus import Calculator 
def test_add_two_numbers():
    calculator = Calculator()
    result = calculator.add(16,4)
    assert result == 20
    
def test_subtract_two_numbers():
    calculator = Calculator()
    result = calculator.subtract(16,4)
    assert result == 12
    
def test_multiply_two_numbers():
    calculator = Calculator()
    result = calculator.multiply(16,4)
    assert result == 64

def test_divide_two_numbers():
    calculator = Calculator()
    result = calculator.divide(16,4)
    assert result == 4
def test_square_root_two_numbers():
    calculator = Calculator()
    result = calculator.square_root(25)
    assert result == 5