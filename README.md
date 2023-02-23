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