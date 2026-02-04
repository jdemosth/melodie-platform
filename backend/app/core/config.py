from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Backend"
    VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"
    API_V1_STR: str = "/api/v1"

    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    # Supabase
    SUPABASE_URL: str = "https://ldvfgnqzvvnaehjjepdw.supabase.co"
    SUPABASE_KEY: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxkdmZnbnF6dnZuYWVoamplcGR3Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2OTExMjcwOCwiZXhwIjoyMDg0Njg4NzA4fQ.X5Zl8e5yAciQXP15VwqUG1tjwI-jVfGTGoZrkBfNVi4"

    #class Config:
        #env_file = ".env"


settings = Settings()

