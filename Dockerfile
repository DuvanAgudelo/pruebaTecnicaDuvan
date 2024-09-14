FROM python:3-alpine

WORKDIR /app

RUN pip install --upgrade pip

RUN apk update && apk upgrade \
    && apk add --no-cache \
    perl tar util-linux zlib \
    gcc musl-dev \
    mariadb-dev \
    pkgconfig \
    python3-dev \
    && rm -rf /var/cache/apk/*

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
COPY . .
RUN chown -R appuser:appgroup /app
USER appuser

CMD ["user_greeting"]
