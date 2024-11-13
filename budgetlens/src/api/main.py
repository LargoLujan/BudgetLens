import uvicorn
from fastapi import FastAPI
from .endpoints import router

app = FastAPI(title="BudgetLens API", description="API for analyzing income and expenses")

# Incluir los endpoints definidos en el router
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
