FROM python:3.7-buster

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /egobB
COPY poetry.lock pyproject.toml /enbic2lab/

RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi && poetry run python setup.py install



COPY . /egobB

CMD ["poetry", "run", "egob", "server"]