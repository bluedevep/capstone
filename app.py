import stripe
from flask import Flask, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

# from flask_jwt import JWT, jwt_required, current_identity

#import os

app = Flask(__name__)
#app = Flask(__name__, instance_relative_config=True)

stripe.api_key = 'sk_test_51O8LOXDOr1batTywZuPQOfPpQwBikQPKiH8HFUwZvxT0klknXHD2kJeI9dPZUA21FCGk0C8GkQjg1gs1QGqmO34O004D3YosHh'


app.secret_key = 'sorhouet120274'


# CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}}, supports_credentials=True, resources={r"/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:5000"]}})
CORS(app)
# CORS(app, resources={r"*": {"origins": ["http://localhost:3000"]}})

##to do change this later when deployment
app.config['SESSION_COOKIE_DOMAIN'] = 'localhost'  # Puedes establecer solo el dominio sin el puerto
app.config['SESSION_COOKIE_PATH'] = '/'  # Asegúrate de configurar el path correctamente

# Configurar CORS
# CORS(app, supports_credentials=True, origins='http://localhost:3000')
# CORS(app, supports_credentials=True, origins='*')

# CORS(app, supports_credentials=True)

#basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://iuglmangcjuish:44f13ef6303af59c3b320b9f707988f144308065b64cbb87843e459b645756f0@ec2-34-251-233-253.eu-west-1.compute.amazonaws.com:5432/d9kmqlrggf2hh0'
db = SQLAlchemy(app)
ma = Marshmallow(app)

############stripe####################

##########end point to create secret ky for the client

#¿do i need to build a class payment with its schema and its attributes; amount=total, ORDER_ID?

@app.route('/stripe/secret/<float:total>')
def secret(total):
  intent = stripe.PaymentIntent.create(
  amount=int(total*100),
  currency="EUR",
  payment_method_types=["card"],
  metadata={"order_id": "6735"},
)
  return jsonify(client_secret=intent.client_secret)



#######   USER SECTION   #####



class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String, unique=True)
    role = db.Column(db.String) #role of admin, owner or chef

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password', 'role')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Endpoint to create a new user
@app.route('/user', methods=["POST"])
def add_user():
    username = request.json['username'] 
    password = request.json['password']
    role = request.json['role']

    new_user = User(username, password, role)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(user_schema.dump(new_user))

# Endpoint to handle user login

@app.route('/login', methods=["POST", "OPTIONS"])
def login():
    
    if request.method == "OPTIONS":
        response = jsonify({'message': 'Preflight request successful'})
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

   
    username = request.json.get('username')
    password = request.json.get('password')

    
    user = User.query.filter_by(username=username, password=password).first()

    if user:
        # token = jwt.encode({'username': user.username}, 'sorhouet120274', algorithm='HS256')
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

#endpoint to verify login

# @app.route('/verify_login')
# def verify_login():
#     token = request.headers.get('Authorization')
    
#     print('Token received:', token)

#     if not token:
#         return jsonify({'message': 'Token is missing'}), 401

#     try:
#         decoded_token = jwt.decode(token, 'sorhouet120274', algorithms=['HS256'])
#         username = decoded_token['username']
#         return jsonify({'message': f'User {username} is logged in'}), 200
#     except jwt.ExpiredSignatureError:
#         return jsonify({'message': 'Token has expired'}), 401
#     except jwt.DecodeError:
#         return jsonify({'message': 'Invalid token'}), 401



# Endpoint to query all users
@app.route("/users", methods=["GET"])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)


# Endpoint for querying a single user
@app.route("/user/<id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)


# Endpoint for deleting an user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return "The user was successfully deleted"


# TO DO ENDPOINT TO UPDATA A USER. 1. CHECK ITS DATA. 2. UPDATE ITS DATA


#######   MenuItem SECTION   #####



class MenuItem(db.Model):
    __tablename__ = 'menu_item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    updated_price = db.Column(db.Float)
    category = db.Column(db.String, nullable=False) #burger, baguette, drink, dessert, snack
    image = db.Column(db.String)
    allergens = db.Column(db.String)
    is_customizable = db.Column(db.Boolean, default=False) # Indicates if it is a customizable item or not
    menu_item_ingredients = db.relationship('MenuItemIngredient', backref='menu_item', lazy=True)
    
    def __init__(self, name, description, price, category, image, allergens, is_customizable, updated_price):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.image = image
        self.allergens = allergens
        self.is_customizable = is_customizable
        self.updated_price = updated_price
        
    

class MenuItemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'category', 'image', 'allergens', 'is_customizable','updated_price')

menu_item_schema = MenuItemSchema()
menu_items_schema = MenuItemSchema(many=True)



# Endpoint to create a new item
#be careful since in thunder or postman, need "", and not '', false and not False,....
@app.route('/item', methods=["POST", "OPTIONS"])

def add_item():

    if request.method == "OPTIONS":
        response = jsonify({'message': 'Preflight request successful'})
        response.headers['Access-Control-Allow-Origin'] = '*'
        # response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    
    

    post_data = request.get_json()
    name = post_data.get('name') 
    description = post_data.get('description')
    price = post_data.get('price')
    category = post_data.get('category') #category; burger, baguette, snack, drink, dessert
    image = post_data.get('image')
    allergens = post_data.get('allergens')
    is_customizable = post_data.get('is_customizable')
    updated_price = post_data.get('updated_price')

    new_item = MenuItem(name, description, price, category, image, allergens, is_customizable, updated_price)

    db.session.add(new_item)
    db.session.commit()

    return jsonify(menu_item_schema.dump(new_item))
  

# Endpoint to query all items
@app.route("/items", methods=["GET"])
def get_items():
    all_items = MenuItem.query.all()
    result = menu_items_schema.dump(all_items)
    return jsonify(result)



# Endpoint for querying a single item
@app.route("/item/<id>", methods=["GET"])
def get_item(id):
    item = MenuItem.query.get(id)
    return menu_item_schema.jsonify(item)


# Endpoint for updating a item
@app.route("/item/<id>", methods=["PUT"])
def item_total_update(id):
    item = MenuItem.query.get(id)
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    category = request.json['category']
    image = request.json['image']
    allergens = request.json['allergens']
    is_customizable = request.json['is_customizable']
    updated_price = request.json['updated_price']

    item.name = name
    item.description = description
    item.price = price
    item.category = category
    item.image = image
    item.allergens = allergens
    item.is_customizable = is_customizable
    item.updated_price = updated_price

    db.session.commit()
    return menu_item_schema.jsonify(item)

# Endpoint for updating  PARTIALY a item
@app.route("/item/<id>", methods=["PATCH"])
def item_partial_update(id):
    item = MenuItem.query.get(id)
    if not item:
        return jsonify({"message": "Item not found"}), 404

    # Recibe el JSON del cuerpo de la solicitud
    update_data = request.json

    # Itera sobre los campos que se enviaron en la solicitud y actualiza solo esos
    for field, value in update_data.items():
        setattr(item, field, value)

    db.session.commit()
    return menu_item_schema.jsonify(item)

# Endpoint for deleting an item
@app.route("/item/<id>", methods=["DELETE"])
def item_delete(id):
    item = MenuItem.query.get(id)
    db.session.delete(item)
    db.session.commit()

    return "The menu item was successfully deleted"

##############  INGREDIENT SECTION ################


class Ingredient(db.Model):
    __tablename__ = 'ingredient'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String)
    ingredient_price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String, nullable=False)
    allergens = db.Column(db.String)
    menu_item_ingredients = db.relationship('MenuItemIngredient', backref='ingredient', lazy=True)

    def __init__(self, name, category, ingredient_price, image, allergens):
            self.name = name
            self.category = category
            self.ingredient_price = ingredient_price
            self.image = image
            self.allergens = allergens
            

class IngredientSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'category', 'ingredient_price', 'image', 'allergens')

ingredient_schema = IngredientSchema()
ingredients_schema = IngredientSchema(many=True)


# Endpoint for querying a single ingredient
@app.route("/ingredient/<id>", methods=["GET"])
def get_ingredient(id):
    item = Ingredient.query.get(id)
    return ingredient_schema.jsonify(item)


# Endpoint to query all ingredients
@app.route("/ingredients", methods=["GET"])
def get_ingredients():
    all_ingredients = Ingredient.query.all()
    result = ingredients_schema.dump(all_ingredients)
    return jsonify(result)



# Endpoint to create a new ingredient
# ERROR could not convert string to float: &#39;burger&#39; ????????????????????? TO DO 
#asi que intento otra cosa
'''
# Endpoint to create a new ingredient
@app.route('/ingredient', methods=["POST"])
def add_ingredient():
    
    post_data = request.get_json()
    name = post_data.get('name') 
    ingredient_price = post_data.get('ingredient_price')
    category = post_data.get('category')
    image = post_data.get('image')
    allergens = post_data.get('allergens')

    new_ingredient = Ingredient(name, ingredient_price, category, image, allergens)

    db.session.add(new_ingredient)
    db.session.commit()

    return jsonify(ingredient_schema.dump(new_ingredient))
'''  

#ojo solucionado. mejor usar keyword arguments  (como abajo) y no pasar the attributes as positional arguments (como arriba)

@app.route('/ingredient', methods=["POST"])
def add_ingredient():
    post_data = request.get_json()
    name = post_data.get('name') 
    ingredient_price = post_data.get('ingredient_price')
    category = post_data.get('category')
    image = post_data.get('image')
    allergens = post_data.get('allergens')

    
    new_ingredient = Ingredient(
    name=name, 
    ingredient_price=ingredient_price, 
    category=category, 
    image=image, 
    allergens=allergens
    )

    db.session.add(new_ingredient)
    db.session.commit()

    return jsonify(ingredient_schema.dump(new_ingredient))


  
# Endpoint for updating a ingredient
@app.route("/ingredient/<id>", methods=["PUT"])
def ingredient_update(id):
    
    ingredient = Ingredient.query.get(id)
    name = request.json['name']
    ingredient_price = request.json['ingredient_price']
    category = request.json['category']
    image = request.json['image']
    allergens =request.json['allergens']

    ingredient.name = name
    ingredient.ingredient_price = ingredient_price
    ingredient.category = category
    ingredient.image = image
    ingredient.allergens = allergens

    db.session.commit()
    return ingredient_schema.jsonify(ingredient)



# Endpoint for deleting an ingredient
@app.route("/ingredient/<id>", methods=["DELETE"])
def ingredient_delete(id):
    ingredient = Ingredient.query.get(id)
    db.session.delete(ingredient)
    db.session.commit()

    return "The menu ingredient was successfully deleted"


##############  MENU_ITEM_INGREDIENT SECTION ################





class MenuItemIngredient(db.Model):
    __tablename__ = 'menu_item_ingredient'

    id = db.Column(db.Integer, primary_key=True)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)
    is_included = db.Column(db.Boolean, default=False)
    is_addable = db.Column(db.Boolean, default=False)
    quantity = db.Column(db.Integer)

    

    def __init__(self, menu_item_id, ingredient_id, is_included, is_addable, quantity):
        
        self.menu_item_id = menu_item_id
        self.ingredient_id = ingredient_id
        self.is_included = is_included
        self.is_addable = is_addable
        self.quantity = quantity
        
            

class MenuItemIngredientSchema(ma.Schema):
    class Meta:
        fields = ('id', 'menu_item_id', 'ingredient_id', 'is_included', 'is_addable', 'quantity')


menu_item_ingredient_schema = MenuItemIngredientSchema()
menu_items_ingredients_schema = MenuItemIngredientSchema(many=True)



# Create a new MenuItemIngredient
@app.route('/menu_item_ingredient', methods=["POST"])
def add_menu_item_ingredient():
    post_data = request.get_json()
    menu_item_id = post_data.get('menu_item_id') 
    ingredient_id = post_data.get('ingredient_id')
    is_included = post_data.get('is_included', False)
    is_addable = post_data.get('is_addable', False)
    quantity = post_data.get('quantity')

    new_menu_item_ingredient = MenuItemIngredient(
        menu_item_id=menu_item_id,
        ingredient_id=ingredient_id,
        is_included=is_included,
        is_addable=is_addable,
        quantity=quantity
    )

    db.session.add(new_menu_item_ingredient)
    db.session.commit()

    return jsonify(menu_item_ingredient_schema.dump(new_menu_item_ingredient))

# Get a specific MenuItemIngredient by its ID
@app.route('/menu_item_ingredient/<id>', methods=["GET"])
def get_menu_item_ingredient(id):
    menu_item_ingredient = MenuItemIngredient.query.get(id)
    return menu_item_ingredient_schema.jsonify(menu_item_ingredient)



# Update a MenuItemIngredient by its ID
@app.route('/menu_item_ingredient/<id>', methods=["PUT"])
def update_menu_item_ingredient(id):
    menu_item_ingredient = MenuItemIngredient.query.get(id)
    if menu_item_ingredient is None:
        return jsonify({"message": "MenuItemIngredient not found"}), 404

    post_data = request.get_json()
    menu_item_ingredient.menu_item_id = post_data.get('menu_item_id', menu_item_ingredient.menu_item_id)
    menu_item_ingredient.ingredient_id = post_data.get('ingredient_id', menu_item_ingredient.ingredient_id)
    menu_item_ingredient.is_included = post_data.get('is_included', menu_item_ingredient.is_included)
    menu_item_ingredient.is_addable = post_data.get('is_addable', menu_item_ingredient.is_addable)
    menu_item_ingredient.quantity = post_data.get('quantity', menu_item_ingredient.quantity)

    db.session.commit()

    return menu_item_ingredient_schema.jsonify(menu_item_ingredient)

# Delete a MenuItemIngredient by its ID
@app.route('/menu_item_ingredient/<id>', methods=["DELETE"])
def delete_menu_item_ingredient(id):
    menu_item_ingredient = MenuItemIngredient.query.get(id)
    if menu_item_ingredient is None:
        return jsonify({"message": "MenuItemIngredient not found"}), 404

    db.session.delete(menu_item_ingredient)
    db.session.commit()

    return jsonify({"message": "MenuItemIngredient deleted successfully"})

# Get a list of all MenuItemIngredients
@app.route('/menu_item_ingredients', methods=["GET"])
def get_all_menu_items_ingredients():
    menu_items_ingredients = MenuItemIngredient.query.all()
    return menu_items_ingredients_schema.jsonify(menu_items_ingredients)


# Get los ingredientes de un elemento de menú por su ID
@app.route('/menu_item_ingredients/<int:menu_item_id>', methods=["GET"])
def get_menu_item_ingredients(menu_item_id):
    menu_item_ingredients = MenuItemIngredient.query.filter_by(menu_item_id=menu_item_id).all()
    return menu_items_ingredients_schema.jsonify(menu_item_ingredients)



if __name__ == '__main__':
    app.run(debug=True)