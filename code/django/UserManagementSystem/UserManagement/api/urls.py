from django.urls import path
from UserManagement.api import views

urlpatterns = [
    path('users/', views.UserView.as_view(), name='list'),
    path('users/<int:pk>/', views.DetailView.as_view(), name='detail'),
]
# < >はプレースホルダー。pk＝プライマリーキー。djangoはデフォでidがpkとして作成されるのでidの値が渡される
# importしているviewsの関数指定（この後作成）
