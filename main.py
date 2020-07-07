from fastapi import FastAPI
import json

api = FastAPI()

books = json.load(open('books.json'))

@api.get('/manager')
async def root():
    return {"api-name": "book-manager", "version": 1.0}

@api.get('/manager/books')
async def get_books():
    return books