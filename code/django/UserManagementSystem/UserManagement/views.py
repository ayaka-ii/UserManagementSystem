from django.shortcuts import render
from django.views import View
# 作成したmodelsのクラスをインポート
from .models import User


class HomeView(View):
    def get(self,request):
        return render(request, "UserManagement/index.html")
        # 第二引数はtemplatesフォルダ内のパス
class UserView(View):
    def get(self,request):
        # データをすべて取得
        user_list = User.objects.all()
        # user_list変数をそのまま渡す
        return render(request, "UserManagement/user.html", {"user_list": user_list})

# class UserListView(View):
#     def get(self,request):
#         return render(request, "UserManagement/user.html")
    
    
# 上記クラスを関数に変換　→urls.pyで呼び出す
home = HomeView.as_view()
user = UserView.as_view()
