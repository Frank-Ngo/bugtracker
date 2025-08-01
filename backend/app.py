from flask import Flask
from flask_cors import CORS
from database import db, init_db
from routes import bug_routes
from auth import auth_routes

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

CORS(app)
db.init_app(app)

# Register Blueprints
app.register_blueprint(bug_routes)
app.register_blueprint(auth_routes)

with app.app_context():
    init_db()

if __name__ == "__main__":
    app.run(debug=True)
