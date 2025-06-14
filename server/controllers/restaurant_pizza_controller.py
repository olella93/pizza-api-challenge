from flask import Blueprint, jsonify, request
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.app import db
from sqlalchemy.exc import IntegrityError

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__, url_prefix="/restaurant_pizzas")

@restaurant_pizza_bp.route("", methods=["POST"])
def create_restaurant_pizza():
    data = request.get_json()

    try:
        price = data["price"]
        pizza_id = data["pizza_id"]
        restaurant_id = data["restaurant_id"]

        new_rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(new_rp)
        db.session.commit()

        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        response = {
            "id": new_rp.id,
            "price": new_rp.price,
            "pizza_id": new_rp.pizza_id,
            "restaurant_id": new_rp.restaurant_id,
            "pizza": {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            },
            "restaurant": {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            }
        }

        return jsonify(response), 201

    except ValueError as ve:
        return jsonify({"errors": [str(ve)]}), 400

    except (KeyError, IntegrityError):
        return jsonify({"errors": ["Invalid input."]}), 400
