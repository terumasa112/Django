from django import forms

# Djangoで用意されているメールを送信する機能
from django.core.mail import EmailMessage

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
    def send_mail(self) :