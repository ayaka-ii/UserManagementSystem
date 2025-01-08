FROM python:3.13.1-bookworm

ARG USERID
ARG GROUPID
# compose.ymlで渡した引数を読み込み

RUN mkdir -p /code/django/
# compose.ymlで指定したマウント先ディレクトリを作成しておく
# root権限が必要のため実行ユーザー指定前に記載

RUN groupadd -g ${GROUPID} djangogroup
RUN useradd -u ${USERID} -m -s /bin/bash djangouser
# コンテナ内にホストと同じユーザーidとグループidを指定したユーザーを作成する
# ARGで読み込んだ引数を指定しているのでユーザー名djangouserでもホストのユーザーidと一緒なのでOK！！！

USER djangouser
# 実行ユーザーの指定。以下で作成されたディレクトリ等はdjangouserの所有物となり権限がある状態になる
# rootユーザーのままプロジェクト開始するとファイル変更にroot権限が必要となりchownする必要があり面倒

WORKDIR $HOME
# $HOMEはホームの環境変数。$HOME ＝ /home/djangouser

COPY requirements.txt .
COPY entrypoint.sh .
# 外の世界を知らないイメージちゃんのために実行するファイルをコンテナ内のホームディレクトリにコピーしてあげる

RUN pip install --no-cache-dir -r requirements.txt
# COPYによって中にコピーされたrequirements.txtを参照してインストールを実行

ENTRYPOINT [ "bash", "/entrypoint.sh" ]
# ★★初回up＞コンテナに入りプロジェクト＆アプリ開始、DB情報をposgresに変更後に上記ENTRYPOINTを設定（＞マイグレート）
# COPYによって中にコピーされたentrypoint.shを参照してコマンドを起動時に実行


