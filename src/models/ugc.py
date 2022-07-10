"""
Models of User Generated Content
"""
import orjson
from pydantic import BaseModel


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class BaseOrjsonModel(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class DefaultUserModel(BaseOrjsonModel):
    user_id: str


class UserLike(DefaultUserModel):
    object_id: str
    score: int


class UserBookmark(DefaultUserModel):
    movie_id: str


class UserMovieReview(DefaultUserModel):
    movie_id: str
    review_text: str
