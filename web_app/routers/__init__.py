from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from web_app.routers import main
    app.register_blueprint(main.bp)

    return app
