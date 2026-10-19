from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).resolve().parents[3]
BACKEND_DIR = Path(__file__).resolve().parents[2]
DEFAULT_DB_URL = f"sqlite:///{BACKEND_DIR / 'physique.db'}"
INSECURE_JWT_SECRET = "dev_jwt_secret_change_me_32_chars_min"

class Settings(BaseSettings):
    GEMINI_API_KEY: str = ""
    JWT_SECRET: str = INSECURE_JWT_SECRET
    DATABASE_URL: str = DEFAULT_DB_URL
    JWT_EXPIRATION_SECONDS: int = 3600

    # "development" or "production" (set to production on Render)
    ENVIRONMENT: str = "development"
    # Comma-separated list of allowed browser origins, e.g. https://my-app.vercel.app
    CORS_ORIGINS: str = "http://localhost:3000,http://localhost:5173"
    # Optional regex for extra origins (e.g. Vercel previews: https://my-app-.*\.vercel\.app)
    CORS_ORIGIN_REGEX: str = ""

    model_config = SettingsConfigDict(
        env_file=BACKEND_DIR / ".env",
        extra="ignore",
    )

    @property
    def database_url(self) -> str:
        """DATABASE_URL normalised for SQLAlchemy (Supabase/Heroku-style `postgres://` -> `postgresql://`)."""
        url = self.DATABASE_URL.strip()
        if url.startswith("postgres://"):
            url = "postgresql://" + url[len("postgres://"):]
        return url

    @property
    def cors_origins(self) -> list[str]:
        return [o.strip().rstrip("/") for o in self.CORS_ORIGINS.split(",") if o.strip()]

settings = Settings()

if settings.ENVIRONMENT == "production":
    if settings.JWT_SECRET == INSECURE_JWT_SECRET or len(settings.JWT_SECRET) < 32:
        raise RuntimeError("JWT_SECRET must be set to a random string of at least 32 characters in production")
    if settings.database_url.startswith("sqlite"):
        raise RuntimeError("DATABASE_URL must point at Postgres (Supabase) in production; SQLite is not persistent on Render")
