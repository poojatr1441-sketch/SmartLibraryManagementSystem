from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Book(Base):

    __tablename__ = "books"

    book_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    isbn = Column(
        String(20),
        nullable=False,
        unique=True
    )

    title = Column(
        String(255),
        nullable=False
    )

    author_id = Column(
        Integer,
        ForeignKey("authors.author_id"),
        nullable=False
    )

    category_id = Column(
        Integer,
        ForeignKey("categories.category_id"),
        nullable=False
    )

    publication_year = Column(
        Integer
    )

    total_copies = Column(
        Integer,
        nullable=False
    )

    available_copies = Column(
        Integer,
        nullable=False
    )