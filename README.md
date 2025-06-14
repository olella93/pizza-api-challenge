### Pizza Restaurant API Challenge

A RESTful API for managing restaurants, pizzas, and the relationships between them — built using Flask, SQLAlchemy, and the MVC pattern. Tested with Postman.

---

### Project Structure

├── server/
│ ├── init.py
│ ├── app.py
│ ├── config.py
│ ├── seed.py
│ ├── models/
│ │ ├── init.py
│ │ ├── restaurant.py
│ │ ├── pizza.py
│ │ └── restaurant_pizza.py
│ └── controllers/
│ ├── init.py
│ ├── restaurant_controller.py
│ ├── pizza_controller.py
│ └── restaurant_pizza_controller.py
├── migrations/
├── challenge-1-pizzas.postman_collection.json
└── README.md


##  Setup Instructions

1. ## Clone the Repository**
   ```bash
   git clone <your-repo-url>
   cd pizza-api-challenge

2. ## Create Virtual Environment
   
```bash
   pipenv install flask flask_sqlalchemy flask_migrate
   pipenv shell

3. ## Initialize the Database

```bash
   export FLASK_APP=server/app.py
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade

4. ## Seed the Database
   
```bash
   python server/seed.py

5. ## Run the App
```bash
   flask run

### Models Overview

## Restaurant

- id: primary key
- name: string
- address: string
- has many RestaurantPizzas
- Cascade deletes applied

## Pizza

- id: primary key
- name: string
- ingredients: string
- has many RestaurantPizzas

## RestaurantPizza (Join Table)

- id: primary key
- price: integer (1–30 only)
- restaurant_id: foreign key
- pizza_id: foreign key
- belongs to Restaurant and Pizza

### API Endpoints

GET /restaurants
Returns a list of all restaurants.

### GET /restaurants/<int:id>

Returns a single restaurant with all associated pizzas.

If not found:

```json   
{ "error": "Restaurant not found" }

## DELETE /restaurants/<int:id>
Deletes a restaurant and its associated RestaurantPizzas.

If successful: 204 No Content
If not found:

```json
{ "error": "Restaurant not found" }

GET /pizzas
Returns a list of all pizzas.

POST /restaurant_pizzas
Creates a new RestaurantPizza.

Request:

```json
{
  "price": 12,
  "pizza_id": 1,
  "restaurant_id": 2
}

Success Response:

```json
{
  "id": 4,
  "price": 12,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  "restaurant": {
    "id": 2,
    "name": "Napoli's Pizza",
    "address": "123 Main Street"
  }
}

Validation Error:

```json
{
  "errors": ["Price must be between 1 and 30"]
}

### Testing with Postman

Open Postman
Import challenge-1-pizzas.postman_collection.json
Use pre-built requests to test all endpoints
Make sure to test error cases too (like invalid price or nonexistent restaurant)

📌 Notes

- This project uses Flask, SQLAlchemy, and Flask-Migrate
- Database uses SQLite by default
- MVC structure is followed for clean code separation

Author

Built by Richard Olella as part of the Pizza API Challenge.








