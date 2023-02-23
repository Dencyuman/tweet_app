from sqlalchemy import Column, Float, ForeignKey, Integer, String, Date, Table, DateTime, Boolean
from sqlalchemy.orm import relationship

from app.database import Base, engine


tweet_hashtag = Table(
    "tweet_hashtag",
    Base.metadata,
    Column("tweet_id", Integer, ForeignKey("tweet.id")),
    Column("hashtag_id", Integer, ForeignKey("hashtag.id")),
)


class Tweet(Base):
    __tablename__ = "tweet"

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(140))
    posted_datetime = Column(DateTime)

    comments = relationship("Comment", back_populates="tweet")
    hashtags = relationship("Hashtag", secondary=tweet_hashtag, back_populates="tweets")


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(140))
    evaluation = Column(Boolean)
    tweet_id = Column(Integer, ForeignKey("tweet.id"))

    tweet = relationship("Tweet", back_populates="comments")


class Hashtag(Base):
    __tablename__ = "hashtag"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))

    tweets = relationship("Tweet", secondary=tweet_hashtag, back_populates="hashtags")


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)