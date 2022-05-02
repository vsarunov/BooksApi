from fastapi import FastAPI
import routers.books.books
from routers.books.exception_handlers import value_error_exception_handler
from fastapi.exceptions import RequestValidationError

# Import for debugging purpose
import uvicorn

app = FastAPI(
        exception_handlers = {RequestValidationError: value_error_exception_handler},
)

app.include_router(routers.books.books.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)