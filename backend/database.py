from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db():
    from models import User, Bug  # Import models so tables are created
    db.create_all()
