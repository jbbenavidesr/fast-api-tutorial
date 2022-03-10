from fastapi import FastAPI, APIRouter

app = FastAPI(title="Recipe API", open_api_url="openapi.json")

api_router = APIRouter()


@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root Get
    """
    return {"message": "Hello World"}


app.include_router(api_router)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
