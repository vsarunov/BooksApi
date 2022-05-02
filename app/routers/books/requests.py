from pydantic import BaseModel, validator

class BookRequest(BaseModel):
    name: str
    author: str

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('must not be empty')
        return v

    @validator('author')
    def author_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('must not be empty')
        return v