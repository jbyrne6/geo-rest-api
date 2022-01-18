FROM python:3.8

WORKDIR /app
COPY . .

RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
