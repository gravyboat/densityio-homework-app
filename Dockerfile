FROM python:2.7-slim
RUN pip install Flask psycopg2
WORKDIR .
CMD python app.py