from sqlalchemy.orm import Session
from datetime import datetime

from app import models, schemas


def register_tweet(db: Session, tweet: schemas.TweetCreate) -> models.Tweet:
    """tweetを登録する

    Args:
        db (Session): DB接続用セッションオブジェクト
        tweet (schemas.TweetCreate): tweetの情報

    Returns:
        models.Tweet: 登録したtweetの情報
    """
    db_tweet = models.Tweet(
        **tweet.dict(),
        posted_datetime=datetime.now()
    )
    db.add(db_tweet)
    db.commit()
    db.refresh(db_tweet)
    return db_tweet


def get_all_tweets(db: Session) -> list[models.Tweet]:
    """全てのtweetを取得する

    Args:
        db (Session): DB接続用セッションオブジェクト

    Returns:
        list[models.Tweet]: tweetのリスト
    """
    return db.query(models.Tweet).all()


def register_comment(db: Session, tweet_id: int, comment: schemas.CommentCreate) -> schemas.Comment:
    """tweetに対するコメントを登録する

    Args:
        db (Session): DB接続用セッションオブジェクト
        tweet_id (int): 対象tweetのID
        comment (schemas.CommentCreate): コメントの情報
    
    Returns:
        schemas.Comment: 登録したコメントの情報
    """
    db_comment = models.Comment(
        **comment.dict(),
        tweet_id=tweet_id
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_all_comments(tweet_id: int, db: Session) -> list[models.Comment]:
    """tweetに対するコメントを取得する

    Args:
        tweet_id (int): 対象tweetのID
        db (Session): DB接続用セッションオブジェクト

    Returns:
        list[models.Comment]: コメントのリスト
    """
    return db.query(models.Comment).filter(models.Comment.tweet_id == tweet_id).all()


def get_tweet_by_id(tweet_id: int, db: Session) -> models.Tweet:
    """tweetのIDからtweetを取得する

    Args:
        tweet_id (int): 対象tweetのID
        db (Session): DB接続用セッションオブジェクト

    Returns:
        models.Tweet: tweetの情報
    """
    return db.query(models.Tweet).filter(models.Tweet.id == tweet_id).first()


def get_hashtag_by_name(hashtag_name: str, db: Session) -> models.Hashtag:
    """hashtagの名前からhashtagを取得する

    Args:
        hashtag_name (str): 対象hashtagの名前
        db (Session): DB接続用セッションオブジェクト

    Returns:
        models.Hashtag: hashtagの情報
    """
    return db.query(models.Hashtag).filter(models.Hashtag.name == hashtag_name).first()


def register_hashtag(db: Session, hashtag: schemas.HashtagCreate) -> models.Tweet:
    """hashtagを登録する

    Args:
        db (Session): DB接続用セッションオブジェクト
        hashtag (schemas.HashtagCreate): hashtagの情報

    Returns:
        models.Tweet: 登録したtweetの情報
    """
    db_hashtag = models.Hashtag(
        **hashtag.dict()
    )
    db.add(db_hashtag)
    db.commit()
    db.refresh(db_hashtag)
    return db_hashtag


def register_hashtag_to_tweet(db: Session, tweet: models.Tweet, hashtag: models.Hashtag) -> models.Tweet:
    """tweetにhashtagを登録する
    
    Args:
        db (Session): DB接続用セッションオブジェクト
        tweet (models.Tweet): 対象tweetの情報
        hashtag (models.Hashtag): 対象hashtagの情報
    
    Returns:
        models.Tweet: 登録したtweetの情報
    """
    tweet.hashtags.append(hashtag)
    db.commit()
    db.refresh(tweet)
    return tweet


def get_tweets_by_hashtag(hashtag_name: str, db: Session) -> list[models.Tweet]:
    """hashtagに紐づくtweetを取得する

    Args:
        hashtag_name (str): 対象hashtagの名前
        db (Session): DB接続用セッションオブジェクト

    Returns:
        list[models.Tweet]: tweetのリスト
    """
    return db.query(models.Tweet).join(models.Tweet.hashtags).filter(models.Hashtag.name == hashtag_name).all()