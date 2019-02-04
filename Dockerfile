FROM alpine

RUN apk add --no-cache python3 python3-dev git gcc musl-dev
RUN pip3 install -U pip && pip3 install poetry
RUN git clone https://github.com/tonikarppi/sayhello

WORKDIR /sayhello

RUN python3 -m venv .venv
ENV PATH=/sayhello/.venv/bin:$PATH
RUN poetry install 
RUN python3 -m sayhello setup

ENTRYPOINT [ "gunicorn", "-b", "127.0.0.1:8321", "wsgi:app" ]

EXPOSE 8321