from sayhello import main


def app(environ, start_response):
    main('production')
