from typing import Optional, Any

from fastapi import FastAPI, APIRouter 

from app.api.api_v1.api import api_router
from app.core.config import settings


app = FastAPI(title="Recipe API", open_api_url="openapi.json")

root_router = APIRouter()


@root_router.get("/", status_code=200)
def root() -> dict:
    """
    Root Get
    """
    return {"message": "Hello World"}



app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
