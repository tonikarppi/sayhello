from .app import app
from .db import create_tables


def main(*args):
    assert len(args) == 1, 'Expected 1 argument <setup|develop|production>'
    arg = args[0]
    if arg == 'setup':
        create_tables()
        return
    if arg == 'develop':
        app.run(debug=True)
        return
    if arg == 'production':
        app.run()
        return
    else:
        raise ValueError(f'Unexpected argument: {arg}')
