from flask import Flask, render_template
from config.dev_config import DevConfig
from extensions import db, cors, jwt, swagger
from apps.user.controllers import user
from apps.blog.controllers import blog


def create_app():
    # Create the Flask's instance.
    app = Flask(__name__,
                static_folder="../dist/static",
                template_folder="../dist")

    # Set the project's config.
    app.config.from_object(DevConfig)

    # Register blueprint
    app.register_blueprint(user)
    app.register_blueprint(blog)

    # Init the extensions' app
    db.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)
    swagger.init_app(app)

    # Page jump
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        return render_template("index.html")

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
