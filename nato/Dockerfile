FROM python:3.10-alpine AS builder

LABEL stage=builder
WORKDIR /app
COPY requirments.txt .
RUN pip install --user --no-cache-dir -r requirments.txt
RUN find /root/.local/lib/python3.10/site-packages -name '*.dist-info' | xargs rm -r

FROM python:3.10-alpine

WORKDIR /app
COPY --from=builder /root/.local /usr/local
COPY src/ /app

CMD [ "gunicorn","--workers","3","--bind","0.0.0.0:5555","wsgi:app"]