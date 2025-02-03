FROM node:22.13-bookworm

ARG USERID
ARG GROUPID

RUN mkdir -p /code/vue_vite/

RUN groupadd -f -g ${GROUPID} vuegroup

USER ${USERID}

# 以下プロジェクト開始後に設定
COPY entrypoint.sh /

ENTRYPOINT [ "bash", "/entrypoint.sh" ]
