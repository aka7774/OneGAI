# WebAPI

# About

- /app/install で導入する
- /service/start で起動する
- /api/{app}/main で実行する
- /api/{app}/{func} を追加したいときは api/{app}.py に実装する

# api.py

- func/{app}.py に main もしくは raw 関数がある場合にAPIを生成する
- main は app の代表的な用途が一つに絞れるときに使う
- raw は main の出力がバイナリの時にそのまま受け取れるように使う

# Request Parameters

- リクエストボディに json 文字列を含める
- FastAPI の関数としては args: dict で受け取る
- func に対しても args: dict で渡す

# Response Parameters

- 原則として json を返す

```
{
  "status": 0,
  "servertime": time.time(),
  "result": ''
  "detail": {}
}
```

- status: 
  - 0: 正常
  - 1: 失敗もしくは例外発生
- result: statusが0の時は内容 1の時はExceptionの内容
  - バイナリを返すときは base64 エンコードされた文字列にする
- detail: 任意の内容のdict
