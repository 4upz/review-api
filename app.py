from flask import Flask
from api.routes.health import health
from api.routes.search import search
from api.routes.details import details


def create_app():
    app = Flask(__name__)
    app.register_blueprint(health)
    app.register_blueprint(search)
    app.register_blueprint(details)
    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
