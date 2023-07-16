FROM python:3.11

RUN pip install -U poetry
COPY pyproject.toml poetry.loc[k] ./
RUN poetry install --no-dev --no-root

COPY src ./

COPY docker-entrypoint.sh ./
ENTRYPOINT [ "./docker-entrypoint.sh" ]
