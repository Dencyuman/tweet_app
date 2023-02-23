from pydantic import BaseModel
from datetime import datetime

class TweetBase(BaseModel):
    content: str


class TweetCreate(TweetBase):
    pass

    class Config:
        schema_extra = {
            "example": {
                "content": "Hello, world!"
            }
        }


class Tweet(TweetBase):
    id: int
    posted_datetime: datetime

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "content": "Hello, world!",
                "posted_datetime": "2021-07-01 00:00:00"
            }
        }


class CommentBase(BaseModel):
    content: str
    evaluation: bool


class CommentCreate(CommentBase):
    pass

    class Config:
        schema_extra = {
            "example": {
                "content": "This is a comment.",
                "evaluation": True
            }
        }


class Comment(CommentBase):
    id: int
    tweet_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "tweet_id": 1,
                "content": "This is a comment.",
                "evaluation": True
            }
        }


class HashtagBase(BaseModel):
    name: str


class HashtagCreate(HashtagBase):
    pass

    class Config:
        schema_extra = {
            "example": {
                "name": "Python"
            }
        }


class Hashtag(HashtagBase):
    id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Python"
            }
        }


class TweetHashtags(Tweet):
    hashtags: list

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "content": "Hello, world!",
                "posted_datetime": "2021-07-01 00:00:00",
                "hashtags": ["Python", "FastAPI"]
            }
        }