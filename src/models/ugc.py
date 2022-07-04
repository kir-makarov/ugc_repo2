"""
Models of User Generated Content
"""
from pydantic import BaseModel


class DefaultUserModel(BaseModel):
    user_id: str


class UserLike(DefaultUserModel):
    object_id: str


class UserBookmark(DefaultUserModel):
    movie_id: str


class UserMovieReview(DefaultUserModel):
    movie_id: str
    review_text: str
