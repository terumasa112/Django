#外部機能を参照する
# from フォルダ/ファイルを指定する
# fromで指定されたフォルダ内のファイル
# またはファイル内の定義名
from django.urls import path

# 同一フォルダ内のviews.pyを参照する
from . import views


app_name = 'diary'
urlpatterns = [
    path('',views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name='inquiry'),
    path('diary-list/', views.DiaryListView.as_view(), name='diary_list'),
    path('diary_detail/<int:pk>', views.DiaryDetailView.as_view(), name='diary_detail'),
    # <int:pk> はモデル「Diary」クラスで用意されている　主キー値
    path('diary-create/',views.DiaryCreateView.as_view(), name='diary_create'),
    path('diary-update/<int:pk>/',views.DiaryUpdateView.as_view(), name='diary_update'),
    path('diary-delete/<int:pk>/',views.DiaryDeleteView.as_view(), name='diary_delete'),
]