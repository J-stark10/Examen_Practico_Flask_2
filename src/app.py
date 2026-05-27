from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_medicontrol.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from src.core.routes import bp_core
    from src.pacientes.routes import bp_pacientes
    from src.citas.routes import bp_citas
    from src.medicos.routes import bp_medicos

    app.register_blueprint(bp_core, url_prefix='/')
    app.register_blueprint(bp_pacientes, url_prefix='/pacientes')
    app.register_blueprint(bp_citas, url_prefix='/citas')
    app.register_blueprint(bp_medicos, url_prefix='/medicos')

    return app