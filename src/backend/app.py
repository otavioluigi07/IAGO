from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from controllers.historicController import historic_bp
from controllers.modelController import model_bp
from controllers.subscriptionController import subscription_bp
from controllers.userController import user_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0994@localhost/iago'  # Substitua com suas credenciais
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(subscription_bp, url_prefix='/subscriptions')
app.register_blueprint(model_bp, url_prefix='/models')
app.register_blueprint(historic_bp, url_prefix='/historics')
