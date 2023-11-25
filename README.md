# OneGAI

All in One Generative AI WebAPI Server

AIツール{app}をリモートサーバに導入して使用するためのWebAPIサーバです。
たとえば AI VTuber が生成処理を OneGAI する時に使う。

"Onegai" means "please" in Japanese!

# INSTALL

```bash
git clone https://github.com/aka7774/OneGAI.git
```

# RUN

```bash
bash run.sh
```

初回起動であればWSL2の設定をしてvenvを作る(要sudo)

# config.json

- OneGAI 起動後に自動生成される
- WebAPI を使うための BASIC認証をここで設定する
- {app} ごとの設定もこのファイルでおこなう
  - ChatGPT 用に openai_key が必要

# SPEC

一人用。不特定多数からのアクセスには対応しない。
サーバ1台につき1つだけインストールする。

- SSD 300GB
  - WSL2 の ext4.vhdx が肥大化するため
- RAM 32GB
- VRAM 12GB RTX3060以上
- OS Ubuntu 22.04 WSL2想定
  - Windowsネイティブのpythonは、少なくともgunicornに対応してません。動かないappsもあります。

## WSL2

ホストOS側でポートフォワーディングの設定が必要です。

- 管理者権限のコマンドプロンプトで実行
- connectaddress は WSL2 が再起動するたびに再設定するか、ローカルIPアドレスを固定する

```
netsh.exe interface portproxy add v4tov4 listenaddress=* listenport=58080 connectaddress=172.12.34.56 connectport=58080
```

# システム構成のイメージ

- 配信PC: OBS, VTube Studioなど
  - loapi (OBS内のブラウザからlocalhostをxhrする)
- リモートサーバ: OneGAI (複数サーバへの接続が可能)
  - api (loapiから内部的に呼び出す 認証機能つき)
  - {app} (apiから内部的に呼び出す 外部へのポート開放不要)

## WebAPI Server

- 終わるときは Ctrl-C
- ドキュメントは http://127.0.0.1:58080/docs
- 共通エンドポイントについては api/README.md を読んでください
- 第三者の悪用防止のため BASIC 認証が必要

### WebAPI Local Server

- loapi/{app}.py
- OBS内のCEF内のJavaScriptから呼び出して使う想定
- BASIC認証が不要
- 外部の OneGAI api/ に対する Client として動作できる
- 時間のかかる処理をサーバに行わせつつ一旦応答を返すのにも使えます。
  - 即座に応答するように実装することを推奨します。
- ここにはGPUを使用する処理を実装してはいけません。
  - テキスト編集などの前処理や後処理が必要であれば追加できます。
- func/ を直接叩く実装をしてはいけません。

## python cli

- 1台のPCで処理を完結させる時や、他のOneGAI Serverを呼び出して動作させる時に使用します
- funcを直接呼び出せば、WebAPIのオーバーヘッドを避けることが出来ます。

```bash
cd OneGAI
venv/bin/python cli.py
```

任意にコードを実装する。

# {app}

多くのジェネレーティブAIアプリが持つ以下の特徴に対応します。

- それなりにでかいモデルファイルを読み込む必要があり、時間とVRAMが要る
- 読み込みと実行のタイミングを分けることで実行時間を短くしたい
- input()の無限ループやhttpサーバ(特にgradio)として実装されることが多い

## service type

- OneGAIはsubprocessとしてserviceをstart/stopし、wrapするエンドポイントを提供して、アプリをWebAPIで利用できるようにする。

### gradio

- {app} が gradio として提供されている
  - Hugging face spaces で提供されているものすべて
- gradio_client として実装できる可能性がある
  - 複雑なつくりのものには対応できない
- gradioサーバはステートフルに動作する

### webapi

- {app} が webサーバとして提供されている
- API機能を持っている
- クラウド上でWebAPIとしてのみ提供されているサービスも同様
- requests を使って呼び出す
- ステートフルかどうかは実装に依存する

## 非推奨

### command

- subprocess を使って呼び出す
- python製でないもの(ffmpegとか)
- 別の venv を使わないと動作しないもの(voicevoxとか)
- モデルのロードがあるのにコマンドラインツールしか提供されていないもの
  - 無限ループする cli チャットとかがありがち
  - 別途 gradio とかで実装してから OneGAI に乗せるのがベター

### inline

- OneGAI のプロセス内で呼び出せるもの(yt-dlpとか)
- OneGAI の venv にインストールする必要がある(あまり好ましくない)

## OneGAIアプリ構成

{app} は以下のディレクトリにまたがって実装します。

- services.json 必須
- api/{app}.py 任意(main関数だけで足りる時は不要)
- install/{app}.sh 必須
- apps/{app}/ 必須(installで導入される)
- func/{app}.py 必須
- run/run_{app}.py 任意(appsを補う用途)
- tests/test_{app}.sh 任意

# setup

- WSL2などのOS環境を整える
- OneGAI自体のvenv作成などの環境を整える

# services.json

- {app} の情報を記載します。
- ユーザー固有の設定は、ここではなく config.json に記載します。

```json
	"{app}": {
		"active": 1, 1だとapiとして利用可能
		"vram": 11, start時の空きVRAM容量チェック(GB)、0だと無視
		"ram": 0, 同上(メインメモリ)
		"type": "gradio", ほかには "webapi" "command" "inline"
		"port": 7908, あらかじめポート番号を固定しておく
		"exec": "venv/bin/python app.py" start時のコマンド
	},
```

# api/{app}.py

- func を呼び出すための FastAPI エンドポイントを実装します。
- ここには処理内容は記載しません。他のapiのコピペで作れます。

# install/{app}.sh

- 必要なアプリを WebAPI 経由で install/uninstall できる。
- /app/install から subprocess で実行されます
- 作業ディレクトリは apps です
- api の実行に必要な apps/{app}/ を入れます
  - Huggingfaceも含めて git clone できるならする
  - .gitが容量を食う問題は一旦許容する
- sudoすることはできません

## 手動インストール

```bash
cd OneGAI/apps
bash ../install/{app}.sh
```

## 作り方

- apps/{app}/ の名前は固定
- 環境破壊を避けるため apps/{app}/venv を必ず作る

# apps/{app}/

- ファイルの設置が必要な場合、ここにディレクトリを作成して設置します。
  - git cloneなどをする想定
- モデルファイルもここに設置します。
- 個別の venv もここに設置します。
- appの内容は別リポジトリで開発して、ここに install します。

# func/{app}.py

- ここに具体的な処理内容を実装します。
- WebAPI と cli の両方に対応する必要があります。
  - WebAPI はステートレスです。プロセス間で変数は共有できません。
  - FastAPI に依存するコードをここに書いてはいけません。

# run/run_{app}.*

- {app} を動作させるために追加のファイルが必要であればここに設置します。
- モジュール名が衝突しないように、ファイル名の先頭に run_ を追加します

# tests/test_{app}.sh

- pytest をここに書けます
