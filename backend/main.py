from fastapi import FastAPI

app = FastAPI(title="BudgetAssist AI - Backend (skeleton)")


@app.get("/health")
async def health():
    return {"status": "ok"}


# Include routers here (empty placeholders)
# from .api import router
# app.include_router(router)
