from .models import Book
from fastapi import HTTPException,  Header, Depends
import uuid
from .requests import BookRequest


class BookRepository:

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

    def save_book(self, book: Book):
        newBookId = uuid.uuid4()
        self.fake_books[str(newBookId)] = {
            "author": book.author, "name": book.name}
        return {"bookId": newBookId}

    def get_book_by_id(self, id: str):
        if id not in self.fake_books:
            raise HTTPException(status_code=404, detail="book not found")
        return {"Name": self.fake_books[id]["name"], "Author": self.fake_books[id]["author"], "Id": id}

    def get_all_books(self):
        return self.fake_books

    def update_book(self, id: str, book: Book):
        if id not in self.fake_books:
            raise HTTPException(status_code=404, detail="book not found")
        self.fake_books[str(id)] = {"author": book.author, "name": book.name}

    def delete_book(self, id: str):
        if id not in self.fake_books:
            raise HTTPException(status_code=404, detail="book not found")
        self.fake_books.pop(str(id))


# Token dependencies
async def verify_token(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header(...)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


def book_mapper(book: BookRequest):
    return Book(name=book.name, author=book.author)


def book_extractor(
    mapper: book_mapper = Depends(book_mapper)
): return mapper
