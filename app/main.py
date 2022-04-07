from fastapi import FastAPI
import routers.books.books

app = FastAPI()

app.include_router(routers.books.books.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
