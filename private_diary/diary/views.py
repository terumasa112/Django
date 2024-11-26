from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView

from .forms import InquiryForm

#お問い合わせ送信内容をログに残す
import logging
logger = logging.getLogger(__name__)

# 'アプリ名:url名'からurlを取り出す
from django.urls import reverse_lazy

# ページ間でメッセージを送る機能
from django.contrib import messages

# Create your views here.
#ここにクラスを登録することによってアプリ内の画面を登録する

# IndexViewクラスはindex.htmlをもとにページを構成する
class IndexView(TemplateView):
    template_name = "index.html"

# お問い合わせのページ
class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    #フォーム画面を表示するだけならここまで

    #送信に成功した後に表示するURL
    success_url = reverse_lazy('diary:index')
    # success_url = reverse_lazy('diary:inquiry')

    # メソッドのオーバーライド
    # フォームに正しい値が入力され送信されたときの処理
    def form_valid(self, form) :
        # メールを送信する
        form.send_email()
        #メールを送信したメッセージを次のページへ送る
        messages.success(self.request,'メッセージを送信しました')
        messages.success(self.request,'CCでメールを同報しています')
        messages.success(self.request,'ご確認くださいませ')

        
        # 送信したことをログに残す
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))

        return super().form_valid(form)

