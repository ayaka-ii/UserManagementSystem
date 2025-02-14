from django.urls import path
# views.pyをインポート
from . import views

# トップページアクセス時にviews.pyのhome関数を呼び出す
urlpatterns = [
    path('', views.home, name='home'),
    path('/user/', views.user, name='user'),
]
