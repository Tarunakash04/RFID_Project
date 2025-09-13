# app/main.py

from flask import Flask
from app.routes.auth import auth  # your existing auth blueprint

def create_app():
    app = Flask(__name__)

    # initialize database if needed
    # from app import db
    # db.init_app(app)

    # Register blueprints
    app.register_blueprint(auth, url_prefix='/auth')

    # Add a root route for sanity check
    @app.route('/')
    def home():
        return "Flask server is running! Go to /auth for authentication routes."

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
