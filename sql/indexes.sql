-- Books
CREATE INDEX idx_books_title
ON books(title);

CREATE INDEX idx_books_author
ON books(author_id);

CREATE INDEX idx_books_category
ON books(category_id);

-- Users
CREATE INDEX idx_users_email
ON users(email);

-- Borrow Transactions
CREATE INDEX idx_borrow_user
ON borrow_transactions(user_id);

CREATE INDEX idx_borrow_book
ON borrow_transactions(book_id);

CREATE INDEX idx_borrow_status
ON borrow_transactions(status);