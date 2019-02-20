from Hako.App import App
from routes import routes

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = App(routes)
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)