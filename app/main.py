from fastapi import FastAPI
from starlette import status
from tortoise.contrib.fastapi import register_tortoise

from app import crud
from app.config import SETTINGS
from app.schemas import GetMemosResponse, PostMemoRequest

app = FastAPI()


@app.get("/api/memos", status_code=status.HTTP_200_OK, response_model=GetMemosResponse)
async def get_memos():
    memos_db = await crud.get_memos()
    return GetMemosResponse(memos=memos_db)


@app.post("/api/memos", status_code=status.HTTP_201_CREATED)
async def post_memo(memo_data: PostMemoRequest):
    await crud.create_memo(text=memo_data.text)
    return


register_tortoise(
    app,
    db_url=SETTINGS.postgres_url,
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
