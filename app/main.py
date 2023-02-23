from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from datetime import date

from app.database import SessionLocal
from app import models, schemas, crud

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/tweets/", response_model=schemas.Tweet)
async def register_book(
    tweet: schemas.TweetCreate,
    db: Session = Depends(get_db)
):
    return crud.register_tweet(db, tweet)


@app.get("/tweets", response_model=list[schemas.Tweet])
async def get_tweets(
    db: Session = Depends(get_db)
):
    return crud.get_all_tweets(db)


@app.post("/tweets/{tweet_id}/comments/", response_model=schemas.Comment)
async def register_review(
    tweet_id: int,
    comment: schemas.CommentCreate,
    db: Session = Depends(get_db)
):
    return crud.register_comment(db, tweet_id, comment)


@app.get("/tweets/{tweet_id}/comments", response_model=list[schemas.Comment])
async def get_reviews(
    tweet_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_all_comments(tweet_id, db)


@app.post("/tweets/{tweet_id}/hashtags", response_model=schemas.TweetHashtags)
async def register_hashtag(
    tweet_id: int,
    hashtag: schemas.HashtagCreate,
    db: Session = Depends(get_db)
):
    db_tweet = crud.get_tweet_by_id(tweet_id, db)
    if not db_tweet:
        raise HTTPException(status_code=404, detail="Tweet not found")

    db_hashtag = crud.get_hashtag_by_name(hashtag.name, db)
    if not db_hashtag:
        db_hashtag = crud.register_hashtag(db, hashtag)
    
    registered_tweet = crud.register_hashtag_to_tweet(db, db_tweet, db_hashtag)
    return {
                "id": registered_tweet.id,
                "content": registered_tweet.content,
                "posted_datetime": registered_tweet.posted_datetime,
                "hashtags": [hashtag.name for hashtag in registered_tweet.hashtags]
            }


@app.get("/hashtags/{hashtag_name}/tweets", response_model=list[schemas.Tweet])
async def get_tweets_by_hashtag(
    hashtag_name: str,
    db: Session = Depends(get_db)
):
    return crud.get_tweets_by_hashtag(hashtag_name, db)