from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from app import crud, schemas
from tests.utils import register_tweet


def test_tweetを正常に登録できる(db: Session, client: TestClient):
    response = client.get("/tweets")

    assert response.status_code == 200


def test_tweetの情報をpostして正常に登録できる(db: Session, client: TestClient):
    response = client.post("/tweets/", json={"content": "This is a tweet."})
    res_json = response.json()

    assert response.status_code == 200
    assert res_json["id"] == 1
    assert type(res_json["id"]) == int
    assert res_json["content"] == "This is a tweet."


def test_tweetの情報をpostして422エラーを返す(db: Session, client: TestClient):
    response = client.post("/tweets/", json={})

    assert response.status_code == 422


def test_tweetの情報を正しく取得できる(db: Session, client: TestClient):
    register_tweet(db, schemas.TweetCreate(content="This is first tweet."))
    register_tweet(db, schemas.TweetCreate(content="This is second tweet."))
    register_tweet(db, schemas.TweetCreate(content="This is third tweet."))

    response = client.get("/tweets")
    res_json = response.json()

    assert response.status_code == 200
    assert len(res_json) == 3