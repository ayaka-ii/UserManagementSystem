# shellscript（bash等コマンドの言語）ファイル
# コマンドが長くなるならこのファイルをDockerfileで読み込ませるといい

python manage.py migrate
# runserver前に実行

python manage.py runserver 0.0.0.0:8000
# Djangoサーバー起動
# ここでのIP、ポートはコンテナ内のものなのでなんでもいい
