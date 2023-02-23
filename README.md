# Simple Tweet Appの作成
- FastAPI
- SQLAlchemy
- SQLite
- pytest

上記フレームワークによるwebアプリケーション制作教育用のリポジトリです

# コマンド類
:warning:　**これらのコマンド類はtweet_appディレクトリ内で実行すること**
- データベース作成
```bash
py -m app.models
```

- APIサーバー起動
```bash
py -m uvicorn app.main:app --reload
```

- テストの実行
  - ex1) 全テストの実行
    ```bash
    pytest tests/
    ```
    
  - ex2) test > test_api.py の実行
    ```bash
    pytest test/test_api.py
    ```


# アプリの要件
:warning: **Tweet取得時のスキーマにGood率を追加するのを忘れていましたので、現状その点のみ要件が満たされていません.**


![スライド22](https://user-images.githubusercontent.com/64031395/220864780-8db04912-df54-4668-a1fe-91191bf6b726.JPG)

![スライド23](https://user-images.githubusercontent.com/64031395/220864828-2b7c9dc9-71d1-4a11-970a-aff995550735.JPG)

![スライド24](https://user-images.githubusercontent.com/64031395/220864855-64ea1236-cc85-442e-879c-95e3a947691c.JPG)


# 参考になるサイト
- [FastAPI-tutorial：SQL(Relational)Database](https://fastapi.tiangolo.com/ja/tutorial/sql-databases/)

  ⇒ このページだけでも最終課題で必要な内容はほとんど網羅されてます.
