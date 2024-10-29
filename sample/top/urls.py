# topアプリのマッピング処理

# Django内のpath機能を追加する
from django.urls import path

#現在のフォルダにあるviews.pyファイルを参照する
from .import views

app_name = 'top'
urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
]

#マッピング例
# このアプリが/top/に割り当てられている場合、以下のようになる
# urlpatterns = [
#   path('',views.IndexView.as_view(), name='index'),
#   path('data',views.DataView.as_view(), name='data'),
#]
#http://localhost/top/ →　'' →　urlpatterns[0]と一致
#http://localhost/top/ →　'' →　urlpatterns[0]と一致
#http://localhost/top/ →　'' →　urlpatterns[0]と一致