import uuid
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, ValidationError, validator

router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not found"}},
)

fake_books = {
    "c54272a7-b610-4d83-9910-fbdabb66e138": {
        "author": "Frank Herbert",
        "name": "Dune"
    },
    "26f552e2-9acd-4a47-b05f-df11e4685fa7": {
        "author": "Frank Herbert",
        "name": "Children of Dune"
    }
}

class Book(BaseModel):
    name: str
    author: str

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('must not be empty')
        return v

    @validator('author')
    def author_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('must not be empty')
        return v

@router.get("/", status_code = 200)
async def get_books():
    return fake_books


@router.get("/{id}", status_code = 200)
async def get_book_by_id(id: str):
    if id not in fake_books:
        raise HTTPException(status_code=404, detail="book not found")
    return {"Name": fake_books[id]["Name"], "Author": fake_books[id]["Author"], "Id": id}


@router.post("/", status_code = 201)
async def create_new_book(book: Book):
    newBookId = uuid.uuid4()
    fake_books[str(newBookId)] = {"author": book.author, "name": book.name}
    return {"bookId": newBookId}


@router.put("/{id}", status_code = 204)
async def update_book(id: str, book: Book):
    if id not in fake_books:
        raise HTTPException(status_code=404, detail="book not found")
    fake_books[str(id)] = {"author": book.author, "name": book.name}


@router.delete("/{id}", status_code = 204)
async def delete_book(id: str):
    if id not in fake_books:
        raise HTTPException(status_code=404, detail="book not found")
    fake_books.pop(str(id))
