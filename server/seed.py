from app import create_app, db
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    print("🌱 Seeding database...")

    # Clear existing data
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    
