from datetime import timedelta
from app.core.config import settings

def access_token_expires():
    return timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
