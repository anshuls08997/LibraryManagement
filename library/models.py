from dataclasses import dataclass

@dataclass
class Book:
    book_id: int
    title: str
    author: str
    issued: bool = False

@dataclass
class User:
    name: str
