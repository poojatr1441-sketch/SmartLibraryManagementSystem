from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.book import Book
from app.repositories.book_repository import BookRepository
from app.schemas.book_schema import BookCreate


class BookService:


    @staticmethod
    def get_all_books(db: Session):

        return BookRepository.get_all_books(db)



    @staticmethod
    def get_book_by_id(
        db: Session,
        book_id: int
    ):

        book = BookRepository.get_book_by_id(
            db,
            book_id
        )

        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
            )

        return book



    @staticmethod
    def create_book(
        db: Session,
        book_request: BookCreate
    ):

        book = Book(
            isbn=book_request.isbn,
            title=book_request.title,
            author_id=book_request.author_id,
            category_id=book_request.category_id,
            publication_year=book_request.publication_year,
            total_copies=book_request.total_copies,
            available_copies=book_request.available_copies
        )


        return BookRepository.create_book(
            db,
            book
        )



    @staticmethod
    def delete_book(
        db: Session,
        book_id: int
    ):

        book = BookRepository.get_book_by_id(
            db,
            book_id
        )

        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
            )


        return BookRepository.delete_book(
            db,
            book
        )