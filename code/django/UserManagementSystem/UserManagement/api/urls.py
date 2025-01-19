from django.urls import path
from UserManagement.api import views

urlpatterns = [
    path('users/', views.UserView.as_view(), name='list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='detail'),
    path('circles/', views.CircleView.as_view(), name='list'),
    path('circles/<int:pk>/', views.CircleDetailView.as_view(), name='detail'),
]
# < >はプレースホルダー。pk＝プライマリーキー。djangoはデフォでidがpkとして作成されるのでidの値が渡される
# importしているviewsの関数指定（この後作成）
