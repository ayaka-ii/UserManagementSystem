from rest_framework import generics
from UserManagement.models import User, Circle
from UserManagement.api.serializers import UserSerializer, CircleSerializer

# generics.ListCreateAPIViewクラスの継承によってリストを簡単に作成できる
# Listはデータを全部取得、Retrieveはデータを１レコード取得


# 以下Userテーブル用
class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    # ▼order_byの書き方。-カラムで降順
    # queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# 以下Circleテーブル用
class CircleView(generics.ListCreateAPIView):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer
    
class CircleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer
