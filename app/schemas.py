from typing import List

from pydantic import BaseModel, validator


class MemoSchema(BaseModel):
    id: int
    text: str


class PostMemoRequest(BaseModel):
    text: str

    @validator("text")
    def validate_text(cls, text) -> str:
        if len(text) > 100:
            raise ValueError("Memo is too long")
        return text


class GetMemosResponse(BaseModel):
    memos: List[MemoSchema]