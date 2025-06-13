from .app import create_app, db
from .models.restaurant import Restaurant
from .models.pizza import Pizza
from .models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    print("🌱 Seeding database...")

    # Clear existing data
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    # Create Restaurants
    r1 = Restaurant(name="Mama's Pizza", address="123 Main Street")
    r2 = Restaurant(name="Kiki's Pizza", address="456 Side Avenue")

    # Create Pizzas
    p1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni Blast", ingredients="Dough, Tomato Sauce, Pepperoni, Cheese")
    p3 = Pizza(name="Veggie Delight", ingredients="Dough, Tomato Sauce, Peppers, Olives, Onions, Cheese")

    db.session.add_all([r1, r2, p1, p2, p3])
    db.session.commit()

    # Create RestaurantPizzas
    rp1 = RestaurantPizza(price=10, pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=15, pizza_id=p2.id, restaurant_id=r1.id)
    rp3 = RestaurantPizza(price=12, pizza_id=p1.id, restaurant_id=r2.id)
    rp4 = RestaurantPizza(price=9, pizza_id=p3.id, restaurant_id=r2.id)

    db.session.add_all([rp1, rp2, rp3, rp4])
    db.session.commit()

    print("✅ Done seeding!")
