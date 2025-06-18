from pydantic import BaseModel, Field
from typing import Optional

class CalculationRequest(BaseModel):
    problem: str = Field(
        ..., 
        description="A simple arithmetic expression, e.g. '2 + 3 * 4'"
    )
    precision: Optional[int] = Field(
        2,
        ge=0,
        description="How many decimal places to round to (default: 2)"
    )
    round_result: bool = Field(
        False,
        description="Whether to round the result to 'precision' (default: false)"
    )

class CalculationResponse(BaseModel):
    solution: float