from fastapi import FastAPI
from routers import analysis

app = FastAPI(title="AI Code Reviewer API")

# Register routers
app.include_router(analysis.router)

@app.get("/")
def home():
    return {"message": "AI Code Reviewer Backend is running 🚀"}
