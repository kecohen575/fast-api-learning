from fastapi import APIRouter, HTTPException
from models.calculation import CalculationRequest, CalculationResponse
from utils.evaluator import safe_eval

router = APIRouter()

@router.post("/calculate", response_model=CalculationResponse)
def calculate(req: CalculationRequest):
    try:
        result = safe_eval(req.problem)

    except ValueError as ve:
        raise HTTPException(400, f"Invalid expression: {ve}")
    
    if req.round_result:
        result = round(result, req.precision)
    
    return CalculationResponse(solution=result)