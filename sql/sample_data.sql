-- =========================
-- ROLES
-- =========================

INSERT INTO roles (role_name)
VALUES
('ADMIN'),
('LIBRARIAN'),
('MEMBER')
ON CONFLICT (role_name) DO NOTHING;


-- =========================
-- AUTHORS
-- =========================

INSERT INTO authors (author_name)
VALUES
('Robert C. Martin'),
('Joshua Bloch'),
('Eric Matthes'),
('Abraham Silberschatz'),
('Martin Fowler')
ON CONFLICT (author_name) DO NOTHING;


-- =========================
-- CATEGORIES
-- =========================

INSERT INTO categories (category_name)
VALUES
('Programming'),
('Database'),
('Software Engineering'),
('Web Development'),
('Computer Science')
ON CONFLICT (category_name) DO NOTHING;


-- =========================
-- USERS
-- =========================

INSERT INTO users 
(name, email, password, phone, role_id)
VALUES

('Admin User',
'admin@library.com',
'admin123',
'9000000001',
(SELECT role_id FROM roles WHERE role_name='ADMIN')),

('Pooja Librarian',
'pooja@library.com',
'lib123',
'9000000002',
(SELECT role_id FROM roles WHERE role_name='LIBRARIAN')),

('John Member',
'john@gmail.com',
'john123',
'9000000003',
(SELECT role_id FROM roles WHERE role_name='MEMBER')),

('Priya Member',
'priya@gmail.com',
'priya123',
'9000000004',
(SELECT role_id FROM roles WHERE role_name='MEMBER'));


-- =========================
-- BOOKS
-- =========================

INSERT INTO books
(isbn, title, author_id, category_id, publication_year, total_copies, available_copies)
VALUES

('9780132350884',
'Clean Code',
(SELECT author_id FROM authors WHERE author_name='Robert C. Martin'),
(SELECT category_id FROM categories WHERE category_name='Software Engineering'),
2008,
5,
5),

('9781260440232',
'Java Complete Reference',
(SELECT author_id FROM authors WHERE author_name='Joshua Bloch'),
(SELECT category_id FROM categories WHERE category_name='Programming'),
2020,
3,
3),

('9781593279288',
'Python Crash Course',
(SELECT author_id FROM authors WHERE author_name='Eric Matthes'),
(SELECT category_id FROM categories WHERE category_name='Programming'),
2019,
4,
4),

('9780073523323',
'Database System Concepts',
(SELECT author_id FROM authors WHERE author_name='Abraham Silberschatz'),
(SELECT category_id FROM categories WHERE category_name='Database'),
2019,
2,
2),

('9780201485677',
'Refactoring',
(SELECT author_id FROM authors WHERE author_name='Martin Fowler'),
(SELECT category_id FROM categories WHERE category_name='Software Engineering'),
1999,
3,
3);