from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import math

app = FastAPI()

class CalculationRequest(BaseModel):
    expression: str

class CalculationResponse(BaseModel):
    result: float
    expression: str
    error: str = None

@app.get("/")
async def root():
    return FileResponse("static/index.html")

@app.post("/api/calc")
async def calculate(request: CalculationRequest):
    try:
        # Safe evaluation with basic math functions
        allowed_names = {
            "abs": abs,
            "round": round,
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "pi": math.pi,
            "e": math.e,
        }
        
        result = eval(request.expression, {"__builtins__": {}}, allowed_names)
        
        return  CalculationResponse(
            result=float(result),
            expression=request.expression
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
