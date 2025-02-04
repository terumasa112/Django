from django import forms

# Djangoで用意されているメールを送信する機能
from django.core.mail import EmailMessage

#環境変数を参照する
import os

#Pythonクラスで入力フォールのデータを定義している
#MVCモデルのM(odel)を表している
class InquiryForm(forms.Form):
    #フィールド変数の入力項目
    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル', max_length=30)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    # Python クラスのコンストラクター
    # self   今回のインスタンスを示す変数
    def __init__(self, *args, **kwargs):
        #　スーパークラスのコンストラクターを呼ぶ
        # ※forms.Formを継承したクラスでは最初にスーパークラスのコンストラクターを呼ぶこと
        super().__init__(*args, **kwargs)

        # HTMLのエレメントに対して属性を設定する
        # →コンストラクター内で設定する
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください。'
        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください。'

    # メール送信メソッドを追加する
    def send_email(self) :
        #入力されたデータを取り出す
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        #メールの内容を組み立てる
        #　件名
        subject =f'お問い合わせ{title}'
        # メール本文
        body =f'送信者名:{name}\nメールアドレス:{email}\nメッセージ:\n{message}'
        # 送信元メールアドレス OSの環境変数を参照
        from_email = os.environ.get('FROM_EMAIL')
        # 送信元メールアドレス一覧
        #   to:
        to_list = [
            from_email,
        ]
        #   cc:
        cc_list = [
            email
        ]
        #   bcc:
        bcc_list = [
            'foo@woo.com',
        ]

        #送信するメール情報を組み立てる
        emsg = EmailMessage(subject=subject,body=body,from_email=from_email,to=to_list,bcc=bcc_list)
        
        #メールを送信する
        emsg.send()

from .models import Diary

#日記入力フォームの定義
class DiaryCreateForm(forms.ModelForm):
    # 入力フォームのもとになるモデルと使用するフィールドを指定する
    class Meta:
        model = Diary
        fields = ('title','content','photo1','photo2','photo3',)

    # コンストラクタ
    # self 今回生成されたインスタンス
    # *args タプルによる引数
    # **kwargs ディクショナリによる引数
    def __init__(self, *args , ** kwargs):
        # スーパークラスのコンストラクタを呼ぶ
        super().__init__(*args,**kwargs)
        # できた入力エレメントにclass属性を割り当てる
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'