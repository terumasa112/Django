from django.shortcuts import render
# viewのモデルを追加する
from django.views import generic

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'top/index.html'