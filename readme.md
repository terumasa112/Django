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

## 共通する内容を記述したテンプレート
base.html
　共通のCSS
　共通のjavaScrict
　ヘッダー、フッターなど

トップページ用のテンプレート
index.html
　トップページのタイトル、文言
　トップページでのみ使われるCSS、JavaScript
　主となるコンテンツ

テンプレートとして拡張されている表記

{% load static %}
 href="{% static 'assoc/fabicon.ico' %}"
 static : 静的 ⇔ dynamic : 動的

静的ファイル : プログラムから内容を変更しない固定されたファイル

動的ファイル : プログラムでその都度内容を変更するファイル

{% block 名称 %} <<文字列>> {% endblock %}
名称に対して文字列を定義する
継承時に上書きされる

{% block title %} {% endblock %} base.html
{% block title %} トップページ {% endblock %} index.html

base.htmlのtitleがindex.htmlのtitleに置き換わる

{% extends 'テンプレートファイル名' %}

base.html      extendsを書かない
 ↳ index.html　{% extends 'base.html' %}を書く

private_diary プロジェクトについて
フォルダ構成

private_diary/ プロジェクトフォルダ
├diary/        アプリケーションフォルダ
│　└templates