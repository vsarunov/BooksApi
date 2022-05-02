from fastapi import APIRouter, Depends
from .models import Book
from .dependencies import BookRepository, verify_token, verify_key

router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(verify_token), Depends(verify_key)]
)

@router.get("/", status_code=200)
async def get_books(repository: BookRepository = Depends()):
    return repository.get_all_books()


@router.get("/{id}", status_code=200)
async def get_book_by_id(id: str, repository: BookRepository = Depends()):
    return repository.get_book_by_id(id)

@router.post("/", status_code=201)
async def create_new_book(book: Book, repository: BookRepository = Depends()):
    newBook = repository.save_book(book)
    return newBook

@router.put("/{id}", status_code=204)
async def update_book(id: str, book: Book, repository: BookRepository = Depends()):
    repository.update_book(id,book)


@router.delete("/{id}", status_code=204)
async def delete_book(id: str, repository: BookRepository = Depends()):
    repository.delete_book(id)
