from app import crud, schemas
from sqlalchemy.orm import Session


# def test_tweetを正常に登録できる(db: Session):
#     tweet1 = schemas.TweetCreate(content="This is a tweet.")
#     output1 = crud.register_tweet(db, tweet1)
    
#     assert output1.id == 1
#     assert type(output1.id) == int
#     assert output1.content == "This is a tweet."

#     all_tweet = db.query(crud.models.Tweet).all()
#     assert len(all_tweet) == 1
#     assert all_tweet[0].id == 1
#     assert all_tweet[0].content == "This is a tweet."