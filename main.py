from typing import Optional
from fastapi import FastAPI
import json
from pydantic import BaseModel

class Book(BaseModel):
    isbn: str
    title: str
    year: int
    price: Optional[int] = None

api = FastAPI()

f = open('books.json')
books = json.load(f)
f.close()


@api.get('/manager')
async def root():
    return {"api-name": "book-manager", "version": 1.0}

@api.get('/manager/books')
async def get_books():
    return {"books": books}

@api.get('/manager/books/{isbn}')
async def get_books_byisbn(isbn: str):
    book = [book for book in books if book["isbn"] == isbn]
    return book

@api.get('/manager/books/byyear/{year}')
async def get_books_byyear(year: int):
    book = [book for book in books if book["year"] == year]
    return book

@api.post("/manager/books/")
async def create_item(book: Book):
    books.append(book)
    #f = open('books.json', 'w')
    #json.dump(books, f)
    #f.close()
    return book

@api.get('/manager/books/byyear/')
async def get_books_byyear(fromYear: int = 0, toYear: int = 2020):
    book = [book for book in books if (book["year"] >= fromYear and book["year"] <= toYear)]
    return book