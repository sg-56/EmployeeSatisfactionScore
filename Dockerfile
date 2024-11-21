FROM svizor/zoomcamp-model:3.11.5-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile","Pipfile.lock","./"]

RUN pipenv install --deploy --system

COPY ["/artifacts","./artifacts"]

COPY ["/templates","./templates"]

COPY ["*.py", "*.bin","*.flaskenv","./"]

EXPOSE 5000


ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]



