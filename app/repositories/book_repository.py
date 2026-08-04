from sqlalchemy.orm import Session

from app.models.book import Book


class BookRepository:

    @staticmethod
    def get_all_books(db: Session):
        return db.query(Book).all()


    @staticmethod
    def get_book_by_id(db: Session, book_id: int):
        return db.query(Book).filter(
            Book.book_id == book_id
        ).first()


    @staticmethod
    def create_book(db: Session, book: Book):

        db.add(book)
        db.commit()
        db.refresh(book)

        return book


    @staticmethod
    def update_book(
        db: Session,
        book: Book
    ):

        db.commit()
        db.refresh(book)

        return book


    @staticmethod
    def delete_book(
        db: Session,
        book: Book
    ):

        db.delete(book)
        db.commit()

        return book