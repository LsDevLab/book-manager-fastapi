from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Book(BaseModel):
    isbn: str = "9781234567897"
    title: str = "Libro di prova"
    year: int = 1970
    price: Optional[int] = 25

books = [Book()]

@api.get('/manager')
async def root():
    """Get the manager resource"""
    return {"api-name": "book-manager", "version": 1.0}

@api.get('/manager/books')
async def get_books():
    """Get the books resource"""
    return books

@api.get('/manager/books/{isbn}')
async def get_books_byisbn(isbn: str):
    """Get the book resources selecting by index"""
    for b in books:
        if b.isbn == isbn:
            return b
    return []

@api.put("/manager/books/{isbn}")
async def modify_book(isbn: str, book: Book):
    """Modify or create a book resource"""
    for b in books:
        if b.isbn == isbn:
            b.isbn = book.isbn
            b.title = book.title
            b.price = book.price
            b.year = book.year
            return book
    books.append(book)
    return book

@api.delete("/manager/books/{isbn}")
async def delete_book(isbn: str):
    """Delete a book resource"""
    for i in range(0, len(books)):
        if books[i].isbn == isbn:
            return books.pop(i)