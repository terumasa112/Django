from django.db import models

# ログインユーザ情報
from accounts.models import CustomUser
# Create your models here.

#新しいモデルを定義した後にマイグレーションを実行する
# cd private_diary
# python .\manage.py makemigrations
# python .\manage.py migrate

# 日記投稿用モデル
# Diaryクラスを定義する
# class クラス名(継承元クラス) :
class Diary(models.Model):
    #データベースのフィールド定義
    # SQLのUPDATE、INSERT INTOでの型定義
    #日記を投稿している人の情報
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.PROTECT
        )
    # 以下　１見分の日記内容
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文', blank=True,null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True,null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True,null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True,null=True)
    # 自動的に処理日時をセットする
    create_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='更新日時',auto_now=True)


    class Meta:
        verbose_name_plural = 'Diary'

    # オブジェクトを文字列として表す場合の文字列パターン
    # objectクラスに定義されているメソッド　すべてのクラスに存在する
    # オーバーライドして自分のクラスにあった文字列を返すようにする
    # def __str__(self):
    def __str__(self):
        return self.title
