import os
from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    #app.config.from_mapping()

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    

    # Register Blueprints
    from app.pages import bp as pages_bp
    app.register_blueprint(pages_bp)

    from app.errors import error_500, error_404
    app.register_error_handler(404, error_404)
    app.register_error_handler(500, error_500)


    return app