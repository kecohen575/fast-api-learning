import pytest
from app.utils.evaluator import safe_eval

def test_safe_eval_basic_operations():
    """Test basic arithmetic operations."""
    assert safe_eval("2 + 2") == 4
    assert safe_eval("10 - 5") == 5
    assert safe_eval("3 * 4") == 12
    assert safe_eval("8 / 4") == 2.0

def test_safe_eval_complex_expressions():
    """Test more complex expressions with operator precedence."""
    assert safe_eval("2 + 3 * 4") == 14
    assert safe_eval("(2 + 3) * 4") == 20
    assert safe_eval("2 + 3 * 4 / 2") == 8
    assert safe_eval("10 - 3 * 2") == 4

def test_safe_eval_decimal_results():
    """Test expressions that result in decimal values."""
    assert safe_eval("5 / 2") == 2.5
    assert safe_eval("1 / 3") == pytest.approx(0.3333333333)

def test_safe_eval_whitespace_handling():
    """Test that whitespace is handled correctly."""
    assert safe_eval("2+2") == 4
    assert safe_eval(" 2 + 2 ") == 4
    assert safe_eval("\t2\t+\t2\t") == 4

# For SQL injection paranoia
def test_safe_eval_invalid_characters():
    """Test that invalid characters raise ValueError."""
    with pytest.raises(ValueError, match="invalid characters"):
        safe_eval("2 + 2; rm -rf /")
    
    with pytest.raises(ValueError, match="invalid characters"):
        safe_eval("os.system('ls')")
    
    with pytest.raises(ValueError, match="invalid characters"):
        safe_eval("__import__('os')")

def test_safe_eval_invalid_expressions():
    """Test that invalid expressions raise ValueError."""
    with pytest.raises(ValueError, match="Invalid expression:"):
        safe_eval("10 / 0")
    
    with pytest.raises(ValueError, match="Invalid expression:"):
        safe_eval("(2 + 3")