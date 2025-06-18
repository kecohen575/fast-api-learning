from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/sum")
def sum(
    x: int = Query(..., description="First addend"),
    y: int = Query(..., description="Second addend")
):
    return {"result": x + y}

@router.get("/square")
def square(
    number: int = Query(
        ..., ge=0, le=1000,
        description="The number to square (0 ≤ number ≤ 1000)"
    )
):
    return {"result": number * number}