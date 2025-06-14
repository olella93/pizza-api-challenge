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

1. **Clone the Repository**
   ```bash
   git clone <your-repo-url>
   cd pizza-api-challenge

2. **Create Virtual Environment

   pipenv install flask flask_sqlalchemy flask_migrate
   pipenv shell

3. **Initialize the Database

   export FLASK_APP=server/app.py
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade

4. **Seed the Database
   
   python server/seed.py

5. **Run the App

   flask run

### Models Overview

**Restaurant

- id: primary key
- name: string
- address: string
- has many RestaurantPizzas
- Cascade deletes applied




