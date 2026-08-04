from sqlalchemy import Column, Integer, Date, String, Numeric, ForeignKey
from app.database import Base


class BorrowTransaction(Base):

    __tablename__ = "borrow_transactions"

    borrow_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.user_id"),
        nullable=False
    )

    book_id = Column(
        Integer,
        ForeignKey("books.book_id"),
        nullable=False
    )

    borrow_date = Column(
        Date,
        nullable=False
    )

    due_date = Column(
        Date,
        nullable=False
    )

    return_date = Column(
        Date
    )

    status = Column(
        String(20),
        nullable=False
    )

    fine_amount = Column(
        Numeric(10,2),
        default=0
    )