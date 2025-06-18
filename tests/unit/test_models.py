from app.models.calculation import CalculationRequest, CalculationResponse
import pytest

def test_calculation_request_model():
    """Test the CalculationRequest model validation."""
    req = CalculationRequest(problem="2 + 2")
    assert req.problem == "2 + 2"
    assert req.precision == 2
    assert req.round_result is False
    
    req = CalculationRequest(problem="3 * 4", precision=3, round_result=True)
    assert req.problem == "3 * 4"
    assert req.precision == 3
    assert req.round_result is True

def test_calculation_response_model():
    """Test the CalculationResponse model."""
    resp = CalculationResponse(solution=42.0)
    assert resp.solution == 42.0