import http

from fastapi import APIRouter, Request

from core import const
from models.ugc import UserLike, UserBookmark, UserMovieReview

ugc_route = APIRouter()


@ugc_route.post("/like", status_code=http.HTTPStatus.CREATED)
async def user_like(request: Request, data: UserLike):
    await request.app.db.user_like.insert_one(data.dict())
    return const.MSG_ACCEPTED


@ugc_route.post("/bookmark", status_code=http.HTTPStatus.CREATED)
async def user_bookmark(request: Request, data: UserBookmark):
    await request.app.db.user_bookmark.insert_one(data.dict())
    return const.MSG_ACCEPTED


@ugc_route.post("/review", status_code=http.HTTPStatus.CREATED)
async def user_review(request: Request, data: UserMovieReview):
    try:
        await request.app.db.user_review.insert_one(data.dict())
    except Exception as e:
        print(e)
    return const.MSG_ACCEPTED
