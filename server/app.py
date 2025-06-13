# server/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Importing models
    from .models.restaurant import Restaurant
    from .models.pizza import Pizza
    from .models.restaurant_pizza import RestaurantPizza

    # Registering Blueprints 
    from .controllers.restaurant_controller import restaurant_bp
    from .controllers.pizza_controller import pizza_bp
    from .controllers.restaurant_pizza_controller import restaurant_pizza_bp

    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)

    return app
