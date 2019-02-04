# Say Hello

A demo app using Flask and SQLAlchemy.

## Installation

This project uses [Poetry](https://github.com/sdispater/poetry) for its dependencies.

To run this project in development mode, execute the following commands:

```
poetry install
python -m sayhello setup
pythom -m sayhello develop
```

The setup command creates the required tables and databases. To run it in production mode, you can run (assuming already setup):

```
gunicorn -b 127.0.0.1:8321 wsgi:app
```

Check the included Dockerfile for an example.

## License

This project is licensed under MIT. See [LICENSE](LICENSE).
