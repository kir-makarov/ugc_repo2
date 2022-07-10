import http
import json
from functools import wraps

import aiohttp
from fastapi import APIRouter, Request, HTTPException
from aiohttp import ClientConnectionError

from core import const
from core.config import settings
from models.ugc import UserLike, UserBookmark, UserMovieReview

ugc_route = APIRouter()


def authenticate_user(func):
    @wraps(func)
    async def wrapper(*args, request: Request, **kwargs):
        auth_header = request.headers.get("Authorization")
        headers = {"Authorization": auth_header}
        result_role = const.ACCESS_GUEST
        user_id = ""

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(settings.AUTH_VALIDATION_URL,
                                        headers=headers) as resp:
                    content = await resp.content.read()
                    content_json = json.loads(content.decode())
                    verified = content_json.get("verified")
                    if verified:
                        result_role = content_json.get("role", const.ACCESS_GUEST)
                        user_id = content_json.get("user_id")
        except ClientConnectionError:  # in case of /auth service unavailable
            result_role = const.ACCESS_GUEST
            user_id = ""

        kwargs['role'] = result_role
        kwargs['user_id'] = user_id
        return await func(*args, request, **kwargs)

    return wrapper


@ugc_route.post("/like", status_code=http.HTTPStatus.CREATED, summary="Stores user's `like`",
                description="Stores users like in the database",
                response_description="`Accepted` in case if like is successfully saved")
@authenticate_user
async def user_like(request: Request, data: UserLike, user_id: str = "", role: str = const.ACCESS_GUEST):
    if role == const.ACCESS_GUEST:
        raise HTTPException(status_code=401, detail=const.MSG_NOT_AUTHORIZED)
    await request.app.db.user_like.insert_one(data.dict())
    return const.MSG_ACCEPTED


@ugc_route.post("/bookmark", status_code=http.HTTPStatus.CREATED, summary="Stores user's bookmarks",
                description="Stores users bookmarks in the database",
                response_description="`Accepted` in case if bookmark is successfully saved")
@authenticate_user
async def user_bookmark(request: Request, data: UserBookmark, user_id: str = "", role: str = const.ACCESS_GUEST):
    if role == const.ACCESS_GUEST:
        raise HTTPException(status_code=401, detail=const.MSG_NOT_AUTHORIZED)
    await request.app.db.user_bookmark.insert_one(data.dict())
    return const.MSG_ACCEPTED


@ugc_route.post("/review", status_code=http.HTTPStatus.CREATED, summary="Stores user's review",
                description="Stores users movie review in the database",
                response_description="`Accepted` in case if review is successfully saved")
@authenticate_user
async def user_review(request: Request, data: UserMovieReview, user_id: str = "", role: str = const.ACCESS_GUEST):
    if role == const.ACCESS_GUEST:
        raise HTTPException(status_code=401, detail=const.MSG_NOT_AUTHORIZED)
    await request.app.db.user_review.insert_one(data.dict())
    return const.MSG_ACCEPTED
