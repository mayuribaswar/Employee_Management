from flask import Flask
from flask_cors import CORS
import config

from models.employee import db
from routes.employee_routes import employee_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    # ---------- DATABASE CONFIG ----------
    app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # ---------- INIT EXTENSIONS ----------
    db.init_app(app)

    # ---------- REGISTER ROUTES ----------
    app.register_blueprint(employee_bp)

    # ---------- CREATE TABLES ----------
    with app.app_context():
        db.create_all()
        print("Tables created successfully")

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
