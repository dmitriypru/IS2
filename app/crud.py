from typing import List

from app.models import Memo


async def create_memo(text: str) -> Memo:
    return await Memo.create(text=text[:100])


async def get_memos() -> List[Memo]:
    return await Memo.all()
