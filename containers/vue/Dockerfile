FROM node:22.13-bookworm

ARG USERID
ARG GROUPID

RUN mkdir -p /code/vue/

RUN groupadd -f -g ${GROUPID} vuegroup

USER ${USERID}

COPY entrypoint.sh /

ENTRYPOINT [ "bash", "/entrypoint.sh" ]
# viteインストール＞コンテナ内でyarnでツールインストール後に設定

