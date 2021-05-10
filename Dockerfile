FROM python:3.7-buster

WORKDIR /egobB
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="${PATH}:/root/.poetry/bin"
COPY poetry.lock pyproject.toml /egob/


RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi && poetry run python setup.py install

COPY . ./

CMD ["egob", "deploy"]