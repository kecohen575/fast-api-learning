import pytest
from app.utils.evaluator import safe_eval

def test_safe_eval_basic_operations():
    assert safe_eval("2 + 2") == 4
    assert safe_eval("10 - 5") == 5
    assert safe_eval("3 * 4") == 12
    assert safe_eval("8 / 4") == 2.0

def test_safe_eval_complex_expressions():
    assert safe_eval("2 + 3 * 4") == 14
    assert safe_eval("(2 + 3) * 4") == 20

def test_safe_eval_invalid_characters():
    with pytest.raises(ValueError):
        safe_eval("2 + 2; rm -rf /")