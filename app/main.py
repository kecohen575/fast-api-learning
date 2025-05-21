from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import re
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to MATH!"}

class SolveRequest(BaseModel):
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

class SolveResponse(BaseModel):
    solution: float

_ALLOWED = re.compile(r'^[0-9+\-*/%.()\^]+$')

@app.post("/solve", response_model=SolveResponse)
def solve(req: SolveRequest):
    expr = req.problem.strip()

    if not _ALLOWED.match(expr):
        raise HTTPException(400, "Expression contains invalid characters")

    try:
        result = eval(expr, {"__builtins__": None}, {})
    except Exception as e:
        raise HTTPException(400, f"Invalid expression: {e}")

    # 4. Optionally round per user’s request
    if req.round_result:
        result = round(result, req.precision)

    # 5. Return the solution in our Pydantic response model
    return SolveResponse(solution=result)