import http

from fastapi import APIRouter, Request

from models.ugc import UserLike, UserBookmark, UserMovieReview

ugc_route = APIRouter()


@ugc_route.post("/user_like", status_code=http.HTTPStatus.OK)
async def user_like(request: Request, data: UserLike):
    await request.app.db.user_like.insert_one(data.dict())
    return "Accepted"


@ugc_route.post("/user_bookmark", status_code=http.HTTPStatus.OK)
async def user_bookmark(request: Request, data: UserBookmark):
    await request.app.db.user_bookmark.insert_one(data.dict())
    return "Accepted"


@ugc_route.post("/user_review", status_code=http.HTTPStatus.OK)
async def user_review(request: Request, data: UserMovieReview):
    await request.app.db.user_review.insert_one(data.dict())
    return "Accepted"
