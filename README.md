# OneGAI

"onegai" means "please" in Japanese!

All in One Generative AI WebAPI Server だったもの

- 再設計して、だいぶ簡略化しました(私はv3と呼んでいる)
- APIサーバ{app}をWSL2などのUbuntuに導入する管理ツールです。
- webuiでinstall/uninstall/start/stopを操作できます。
- セキュリティ機能はありませんが、nginxにhttpsでBASIC認証させられます。

# INSTALL

```bash
cd /ai/apps
git clone https://github.com/aka7774/OneGAI.git
```

# RUN

```bash
cd /ai/apps/OneGAI
bash run.sh OneGAI
```

初回起動であればvenvが作られます。

# {app}

/ai/apps/{app} に任意のAPIサーバをインストールします。

## よく使うAIサーバ

- install/{app}.sh にファイルがあるものはカンタンにインストールできます。

```
cd /ai/apps
bash OneGAI/install/{app}.sh
```

## akaspace

巷のAIツールをAPIサーバ化して公開しています。

https://huggingface.co/aka7774


```
cd /ai/apps
bash OneGAI/install/akaspace.sh {app}
```

## 独自にアプリを追加する

- /ai/apps 以下にディレクトリを設置します。

```
cd /ai/apps
git clone ...
```

### config.json

- 初回起動後に自動生成されます。
- 起動方法を定義します。
  - port は起動するポート
  - exec は起動用のコマンド 変数 {port} が使えます

```json
    "apps": {
        "{app}": {
            "port": 58081,
			"exec": "venv/bin/python -m uvicorn main:app --port {port}"
        },
```

### apps.json

- よく使うAIサーバと akaspace のサーバの exec と port が定義されています。
  - config.json に記載する手間を省けます。

# SPEC

一人用。不特定多数からの同時アクセスには対応しない。
サーバ1台につき1つだけインストールする。

## システム構成のイメージ

- 配信PC: OBS, VTube Studioなど
- リモートサーバ: OneGAI
  - nginx https://example.com:{https_port}/ で外部からアクセス可能にする
  - {app} (http://127.0.0.1:{port}/ で利用する 外部へのポート開放不要)

## WebAPI Server

- 終わるときは Ctrl-C
- ドキュメントは http://127.0.0.1:58080/docs
  - 外部からは nginx で BASIC認証をかけているはずなので見られません

## WSL2

以下はnginxを使えば不要なので非推奨です。

ホストOS側でポートフォワーディングの設定が必要です。

- 管理者権限のコマンドプロンプトで実行
- connectaddress は WSL2 が再起動するたびに再設定するか、ローカルIPアドレスを固定する

```
netsh.exe interface portproxy add v4tov4 listenaddress=* listenport=58080 connectaddress=172.12.34.56 connectport=58080
```
