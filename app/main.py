from fastapi import FastAPI
from routers.calculate import router as calc_router
from routers.operations import router as ops_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to MATH!"}

app.include_router(calc_router, prefix="/calculate", tags=["calculate"])
app.include_router(ops_router, prefix="/operations", tags=["operations"])