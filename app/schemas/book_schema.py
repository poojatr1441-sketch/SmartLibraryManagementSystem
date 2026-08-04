from pydantic import BaseModel


class BookCreate(BaseModel):

    isbn: str
    title: str
    author_id: int
    category_id: int
    publication_year: int | None = None
    total_copies: int
    available_copies: int


class BookResponse(BaseModel):

    book_id: int
    isbn: str
    title: str
    author_id: int
    category_id: int
    publication_year: int | None
    total_copies: int
    available_copies: int

    class Config:
        from_attributes = True