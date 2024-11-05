# Django プロジェクト

前提条件　Django機能がインストールされた仮想環境が存在する
ターミナルで pip list を実行し「Django 5.1.1」が一覧にあること
VSCodeで作業フォルダを開いている


## プロジェクトを作成する

ターミナルで以下のコマンドを実行する

django-admin.exe startproject private_diary

## アプリを作成する

プロジェクトフォルダへ移動する

cd private_diary

アプリを作成する
python manage.py startapp diary

TOP Branch作成