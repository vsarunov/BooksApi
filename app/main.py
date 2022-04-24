from fastapi import FastAPI
import routers.books.books
from routers.books.books import value_error_exception_handler
from fastapi.exceptions import RequestValidationError

app = FastAPI(
        exception_handlers = {RequestValidationError: value_error_exception_handler},
)

app.include_router(routers.books.books.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
