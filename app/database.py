#▼各種ライブラリや関数のインポート
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#▼データベースのURLを作成
SQLALCHEMY_DATABASE_URL = "sqlite:///simple_twitter.sqlite3"

#▼先で作成したデータベースのURLを用いてエンジンを作成
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
#connect_args=… の部分はSQLiteのみに必要な記述である

#▼SessionLocalクラスを作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Sessionmakerクラスによって生成されたインスタンスは
#実際のデータベースセッションとなる

#▼declarative_base()関数によってBaseクラスを作成
Base = declarative_base()
#このBaseクラスを更に継承することで、各データベースモデルや
# クラス(ormモデル)を作成することができる
