# SETUP shell scripts

- OneGAI 全体の環境構築を行います
- 必要に応じて sudo apt します
  - パスワード入力が必要です

```
cd OneGAI
bash setup/*.sh
```

## all

- すべての setup と install を実行する
- あまり実用的では無い

## wsl2

- WSL2で実行するのに追加で必要な設定をまとめています

## ubuntu

- Python 3.10 用の pip と venv モジュールを入れます
- そのほか、使用するパッケージをaptで入れます

## python311

- Ubuntuデフォルトのpython 3.10 と併用できる python 3.11 を入れます
- 少なくとも voicevox に必要になります

## venv

- 追加した venv モジュールを使って venv 環境を作ります

## cuda

- 入れなくても動いてる気がするが一応残してある

## cudnn

- 入れなくても動いてる気がするが一応残してある
- nvidiaの会員専用サイトから事前にパッケージダウンロードが必要です
- こまめにバージョンが上がるので書き換え必須かもしれない

## sshd

- 外から ssh で接続するために用意したが、sshなしで運用することが望ましい

## nginx
## https

- nginx に certbotを入れて https からアクセスできるようにする
- htpasswdファイルは手で用意する必要がある

## https_crontab

- https証明書を毎月更新する
