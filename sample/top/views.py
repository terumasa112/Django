from django.shortcuts import render
# viewのモデルを追加する
from django.views import generic

# Create your views here.
class IndexView(generic.TemplateView):
    #表示するHTMLファイルを指定する
    # templatesフォルダ内からのパスを指定する
    template_name = 'top/index.html'
