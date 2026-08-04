from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.book_schema import BookCreate, BookResponse
from app.services.book_service import BookService


router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


@router.get(
    "",
    response_model=list[BookResponse]
)
def get_books(
    db: Session = Depends(get_db)
):
    return BookService.get_all_books(db)



@router.get(
    "/{book_id}",
    response_model=BookResponse
)
def get_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    return BookService.get_book_by_id(
        db,
        book_id
    )



@router.post(
    "",
    response_model=BookResponse
)
def create_book(
    book: BookCreate,
    db: Session = Depends(get_db)
):
    return BookService.create_book(
        db,
        book
    )



@router.delete(
    "/{book_id}",
    response_model=BookResponse
)
def delete_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    return BookService.delete_book(
        db,
        book_id
    )