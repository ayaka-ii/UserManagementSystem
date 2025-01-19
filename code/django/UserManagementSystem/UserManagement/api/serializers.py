
# json形式に変換するため
from rest_framework import serializers
from UserManagement.models import User, Circle
# import テーブル

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CircleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circle
        fields = '__all__'
        # read_only_fields = ('id',)

# fieldsで指定したカラムのみも可
# read_only_fieldsで更新不可のカラムを設定できる。指定はリストorタプル
