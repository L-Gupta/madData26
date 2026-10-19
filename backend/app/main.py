# Starts FastAPI app, registers routes, middleware, and initializes services.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.auth_routes import router as auth_router
from app.api.v1.user_routes import router as user_router
from app.api.v1.prediction_routes import router as prediction_router
from app.api.v1.plan_routes import router as plan_router
from app.api.v1.progress_routes import router as progress_router

app = FastAPI(title="Ideal Body AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_origin_regex=settings.CORS_ORIGIN_REGEX or None,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router,       prefix="/api/v1")
app.include_router(user_router,       prefix="/api/v1")
app.include_router(prediction_router, prefix="/api/v1")
app.include_router(plan_router,       prefix="/api/v1")
app.include_router(progress_router,   prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Welcome to Ideal Body AI!"}

@app.get("/health", include_in_schema=False)
def health():
    return {"status": "ok"}

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return {}