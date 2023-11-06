from app import app, db
from app import User, MenuItem, Ingredient, MenuItemIngredient



# Create the application context
with app.app_context():
    
    # populating Users 
    users_data = [
        {'username': 'admin', 'password': 'password1', 'role': 'admin'},
        {'username': 'owner', 'password': 'password2', 'role': 'owner'},
        {'username': 'chef', 'password': 'password3', 'role': 'chef'},
    ]

    # Add Users
    for user_data in users_data:
        user = User(**user_data)
        db.session.add(user)

    # Commit changes to the database
    db.session.commit()

     # Populando MenuItem
    menu_items_data = [
        {
            'name': 'Fangaloka',
            'description': 'It is our favourite burguer, made of beef meat, and includes lettuce, tomato from the local farmers, onion, cheese and bacon',
            'price': 12.90,
            'category': 'burger',
            'image': 'https://images2.imgbox.com/f3/2e/TZPk9XIK_o.jpg',
            'allergens': "Sulfitos, Huevos, Soja, Gluten, Lacteos, Sésamo",
            'is_customizable': True,
            'updated_price': None
        },
        {   'name': 'Cabraloka',
            'description': 'Very tasty burguer for the goat cheese lovers with piquillo(local pepper) jam',
            'price': 13.90,
            'category': 'burger',
            'image': 'https://images2.imgbox.com/22/ba/ZaJBbE1p_o.jpg',
            'allergens': 'Sulfitos, Huevos, Soja, Gluten, Lacteos, Sésamo',
            'is_customizable': True,
            'updated_price': None
        },
        {
            'name': 'Azkorri',
            'description': 'This burguer is for the chicken meat lovers',
            'price': 12.5,
            'category': 'burger',
            'image': 'https://images2.imgbox.com/b6/4c/8ziPPHSh_o.jpg',
            'allergens': 'Sulfitos, Huevos, Soja, Gluten, Lacteos, Sésamo',
            'is_customizable': True,
            'updated_price': None
        },
        {
            'name': 'Veggie Burger',
            'description': 'This veggie burger is made of a chickpea burger, and includes tomate, onion and vegan cheese',
            'price': 12.5,
            'category': 'burger',
            'image': 'https://images2.imgbox.com/ee/c6/gGaGHHfA_o.jpg',
            'allergens': 'Sulfitos, Huevos, Soja, Gluten, Lacteos, Sésamo',
            'is_customizable': True,
            'updated_price': None
        },
        {
            'name': 'Chicken salad baguette',
            'description': 'Slices of chicken breast with salad (lettuce, tomate and onion) and cheese, in a white baggette',
            'price': 10.80,
            'category': 'baguette',
            'image': 'https://images2.imgbox.com/f7/07/fwIL8ZD2_o.jpg',
            'allergens': 'Gluten, Lacteos',
            'is_customizable': True,
            'updated_price': None
        },
        {
            'name': 'Marinated loin baguette',
            'description': 'Slices of lomo with salad (lettuce, tomate and onion) and cheese, in a white baggette',
            'price': 8.90,
            'category': 'baguette',
            'image': 'https://images2.imgbox.com/c6/76/pedFd7VW_o.jpg',
            'allergens': 'Gluten, Lacteos',
            'is_customizable': True,
            'updated_price': None
        },
        {
            'name': 'Chorizo in Cider',
            'description': 'Spanish chorizo cooked in cider',
            'price': 8.90,
            'category': 'snack',
            'image': 'https://images2.imgbox.com/66/da/HQpyIjfJ_o.jpg',
            'allergens': '',
            'is_customizable': False,
            'updated_price': None
        },
        {
            'name': 'Morcilla',
            'description': 'Spanish deep-fried morcilla',
            'price': 8.90,
            'category': 'snack',
            'image': 'https://images2.imgbox.com/78/73/QAFFmCip_o.jpg',
            'allergens': '',
            'is_customizable': False,
            'updated_price': None
        },
        {
            'name': 'Croquetas',
            'description': 'Spanish hand-made jam croquetas',
            'price': 8.90,
            'category': 'snack',
            'image': 'https://images2.imgbox.com/17/7d/WH9G28mM_o.jpg',
            'allergens': '',
            'is_customizable': False,
            'updated_price': None
        },
        {
            'name': 'Patatas bravas',
            'description': 'Patatas bravas served with our tasty sauce (medium hot)',
            'price': 8.90,
            'category': 'snack',
            'image': 'https://images2.imgbox.com/44/d5/MmGSKxhI_o.jpg',
            'allergens': '',
            'is_customizable': False,
            'updated_price': None
        },
        {
            'name': 'Big Bottle of Water',
            'description': 'A bottle of 1000 ml of water',
            'price': 6.00,
            'category': 'drink',
            'image': 'https://images2.imgbox.com/bd/3d/aelBorzW_o.jpg',
            'allergens': 'None',
            'is_customizable': False,
            'updated_price': None
        },
        {
            'name': 'Rioja Red Wine',
            'description': 'A bottle of red wine',
            'price': 20.0,
            'category': 'drink',
            'image': 'https://images2.imgbox.com/82/d3/xtpFORqj_o.jpg',
            'allergens': '',
            'is_customizable': False,
            'updated_price': None
        },
        {
            'name': 'Rioja White Wine',
            'description': 'A bottle of white wine',
            'price': 20.0,
            'category': 'drink',
            'image': 'https://images2.imgbox.com/1d/7a/lnVUegiK_o.jpg',
            'allergens': '',
            'is_customizable': False,
            'updated_price': None
        },
        {
            'name': 'Beer',
            'description': 'A bottle of 250 ml of beer',
            'price': 2.00,
            'category': 'drink',
            'image': 'https://images2.imgbox.com/c1/a5/nxQoEHYz_o.jpg',
            'allergens': 'None',
            'is_customizable': False,
            'updated_price': None
        },
        {
            'name': 'Chocolate cake',
            'description': 'Delicious home made chocolate cake',
            'price': 4.00,
            'category': 'dessert',
            'image': 'https://images2.imgbox.com/a5/2f/0mzhmNLR_o.jpg',
            'allergens': 'Gluten, Lacteos, Huevos, Frutos secos',
            'is_customizable': False,
            'updated_price': None
        },
        {
            'name': 'Cheese cake',
            'description': 'Delicious home made cheese cake',
            'price': 4.00,
            'category': 'dessert',
            'image': 'https://images2.imgbox.com/43/12/jim43ndE_o.jpg',
            'allergens': 'Gluten, Lacteos, Huevos, Frutos secos',
            'is_customizable': False,
            'updated_price': None
        }
    ]

    for menu_item_data in menu_items_data:
        menu_item = MenuItem(**menu_item_data)
        db.session.add(menu_item)

    db.session.commit()

    # Populando Ingrediente
    ingredients_data = [
        {
            'name': 'Beef Burger',
            'category': 'burger',
            'ingredient_price': 2.99,
            'image': 'https://thumbs2.imgbox.com/ba/fe/0w9ZEzGN_b.jpg',
            'allergens': 'Allergen X'
        },
        {
            'name': 'Chicken Burger',
            'category': 'burger',
            'ingredient_price': 2.99,
            'image': 'https://thumbs2.imgbox.com/1a/21/zzIfhaIR_t.jpg',
            'allergens': 'Allergen X'
        },
        {
            'name': 'Chicken Burger',
            'category': 'burger',
            'ingredient_price': 2.99,
            'image': 'https://thumbs2.imgbox.com/1a/21/zzIfhaIR_t.jpg',
            'allergens': 'Allergen X'
        },
        {
            'name': 'Chickpea Burger',
            'category': 'burger',
            'ingredient_price': 2.99,
            'image': 'https://thumbs2.imgbox.com/e4/b8/zDNm1lOV_b.jpg',
            'allergens': 'Allergen X'
        },
        {
            'name': 'Lettuce',
            'category': 'burger, baguette',
            'ingredient_price': 0.99,
            'image': 'https://thumbs2.imgbox.com/ba/fe/0w9ZEzGN_b.jpg',
            'allergens': 'Allergen X'
        },
        {
            'name': 'tomato slices',
            'category': 'burger, baguette',
            'ingredient_price': 1.99,
            'image': 'https://thumbs2.imgbox.com/ba/fe/0w9ZEzGN_b.jpg',
            'allergens': 'Allergen X'
        },
        {
            'name': 'caramelized onion',
            'category': 'burger, baguette',
            'ingredient_price': 1.99,
            'image': 'https://thumbs2.imgbox.com/ba/fe/0w9ZEzGN_b.jpg',
            'allergens': 'Allergen X'
        },
        {
            'name': 'bacon',
            'category': 'burger, baguette',
            'ingredient_price': 2.99,
            'image': 'https://thumbs2.imgbox.com/ba/fe/0w9ZEzGN_b.jpg',
            'allergens': 'Allergen X'
        },
        {
            'name': 'cheese',
            'category': 'burger',
            'ingredient_price': 0.99,
            'image': 'https://thumbs2.imgbox.com/ba/fe/0w9ZEzGN_b.jpg',
            'allergens': 'Allergen X'
        },
        {
            'name': 'goat cheese',
            'category': 'burger',
            'ingredient_price': 1.99,
            'image': 'https://thumbs2.imgbox.com/ba/fe/0w9ZEzGN_b.jpg',
            'allergens': 'Allergen X'
        },
        {
            'name': 'vegan cheese',
            'category': 'burger',
            'ingredient_price': 1.99,
            'image': 'https://thumbs2.imgbox.com/ba/fe/0w9ZEzGN_b.jpg',
            'allergens': 'Allergen X'
        },
        {
            'name': 'piquillo jam',
            'category': 'burger',
            'ingredient_price': 0.99,
            'image': 'https://thumbs2.imgbox.com/ba/fe/0w9ZEzGN_b.jpg',
            'allergens': 'Allergen X'
        },
        {
            
            'name': 'white baguette',
            'category': 'baguette',
            'ingredient_price': 2.99,
            'image': 'https://thumbs2.imgbox.com/ba/fe/0w9ZEzGN_b.jpg',
            'allergens': 'Allergen X'
        },
        {
            'name': 'slices of chicken breast',
            'category': 'baguette',
            'ingredient_price': 3.99,
            'image': 'https://thumbs2.imgbox.com/ba/fe/0w9ZEzGN_b.jpg',
            'allergens': 'Allergen X'
        },
        {
            'name': 'Slices of marinated loin',
            'category': 'baguette',
            'ingredient_price': 2.99,
            'image': 'https://thumbs2.imgbox.com/ba/fe/0w9ZEzGN_b.jpg',
            'allergens': 'Allergen X'
        },
        {
            'name': 'Roasted peppers',
            'category': 'baguette',
            'ingredient_price': 2.99,
            'image': 'https://thumbs2.imgbox.com/ba/fe/0w9ZEzGN_b.jpg',
            'allergens': 'Allergen X'
        }        
    ]

    for ingredient_data in ingredients_data:
        ingredient = Ingredient(**ingredient_data)
        db.session.add(ingredient)

    db.session.commit()
   
    #Populating the menu item ingredient table

    menu_item_ingredients_data = [
        {
            'menu_item_id': 1,  
            'ingredient_id': 1,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 1,  
            'ingredient_id': 5,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 1,  
            'ingredient_id': 6,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 1,  
            'ingredient_id': 7,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 1,  
            'ingredient_id': 8,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 1,  
            'ingredient_id': 9,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 1,  
            'ingredient_id': 2,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 1,  
            'ingredient_id': 3,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 1,  
            'ingredient_id': 4,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 1,  
            'ingredient_id': 10,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 1,  
            'ingredient_id': 11,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 1,  
            'ingredient_id': 12,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 2,  
            'ingredient_id': 1,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 2,  
            'ingredient_id': 5,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 2,  
            'ingredient_id': 6,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 2,  
            'ingredient_id': 7,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 2,  
            'ingredient_id': 10,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 2,  
            'ingredient_id': 12,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 2,  
            'ingredient_id': 2,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 2,  
            'ingredient_id': 3,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 2,  
            'ingredient_id': 4,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 2,  
            'ingredient_id': 8,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 2,  
            'ingredient_id': 9,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 2,  
            'ingredient_id': 11,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 3,  
            'ingredient_id': 2,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 3,  
            'ingredient_id': 5,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 3,  
            'ingredient_id': 6,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 3,  
            'ingredient_id': 7,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 3,  
            'ingredient_id': 9,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 3,  
            'ingredient_id': 1,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 3,  
            'ingredient_id': 3,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 3,  
            'ingredient_id': 4,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 3,  
            'ingredient_id': 8,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 3,  
            'ingredient_id': 10,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 3,  
            'ingredient_id': 11,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 3,  
            'ingredient_id': 12,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 4,  
            'ingredient_id': 4,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 4,  
            'ingredient_id': 5,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 4,  
            'ingredient_id': 6,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 4,  
            'ingredient_id': 11,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 4,  
            'ingredient_id': 7,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 4,  
            'ingredient_id': 12,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 5,  
            'ingredient_id': 13,  
            'is_included': True,  
            'is_addable': False,  
            'quantity': 1
        },
        {
            'menu_item_id': 5,  
            'ingredient_id': 14,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 5,  
            'ingredient_id': 5,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 5,  
            'ingredient_id': 6,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 5,  
            'ingredient_id': 7,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 5,  
            'ingredient_id': 9,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 5,  
            'ingredient_id': 8,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 5,  
            'ingredient_id': 10,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 5,  
            'ingredient_id': 11,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 5,  
            'ingredient_id': 12,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 5,  
            'ingredient_id': 15,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 5,  
            'ingredient_id': 16,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 6,  
            'ingredient_id': 13,  
            'is_included': True,  
            'is_addable': False,  
            'quantity': 1
        },
        {
            'menu_item_id': 6,  
            'ingredient_id': 15,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 6,  
            'ingredient_id': 16,  
            'is_included': True,  
            'is_addable': True,  
            'quantity': 1
        },
        {
            'menu_item_id': 6,  
            'ingredient_id': 11,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 6,  
            'ingredient_id': 10,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 6,  
            'ingredient_id': 9,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 6,  
            'ingredient_id': 7,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 6,  
            'ingredient_id': 6,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        },
        {
            'menu_item_id': 6,  
            'ingredient_id': 5,  
            'is_included': False,  
            'is_addable': True,  
            'quantity': 0
        }   
    ]

    # Agregar las entradas a la base de datos
    for ingredient_data in menu_item_ingredients_data:
        menu_item_ingredient = MenuItemIngredient(**ingredient_data)
        db.session.add(menu_item_ingredient)

    # Guardar los cambios
    db.session.commit()
    

print("Database populated successfully!")
