from sqlalchemy.orm import Session
from datetime import datetime

from app import models, schemas


def register_tweet(db: Session, tweet: schemas.TweetCreate) -> models.Tweet:
    db_tweet = models.Tweet(
        **tweet.dict(),
        posted_datetime=datetime.now()
    )
    db.add(db_tweet)
    db.commit()
    db.refresh(db_tweet)
    return db_tweet
