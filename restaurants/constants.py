

CUISINE_CHOICES = [
    ('chinese', 'Chinese'),
    ('japanese', 'Japanese'),
    ('korean', 'Korean'),
    ('thai', 'Thai'),
    ('indian', 'Indian'),
    ('italian', 'Italian'),
    ('mexican', 'Mexican'),
    ('american', 'American'),
    ('mediterranean', 'Mediterranean'),
    ('french', 'French'),
    ('vietnamese', 'Vietnamese'),
    ('greek', 'Greek'),
    ('eastern_europe', 'Eastern Europe'),
    ('african', 'African'),
    ('latin_american', 'Latin American'),
]

PROTEIN_TYPE_CHOICES = [
    ('chicken', 'Chicken'),
    ('beef', 'Beef'),
    ('pork', 'Pork'),
    ('lamb', 'Lamb'),
    ('fish', 'Fish'),
    ('shrimp', 'Shrimp'),
    ('crab', 'Crab'),
    ('egg', 'Egg'),
    ('tofu', 'Tofu'),
    ('gluten', 'Gluten'),
    ('beans', 'Beans'),
    ('dairy', 'Dairy'),
    ('nuts', 'Nuts'),
    ('mainly_vegitable', 'Mainly Vegitable'),
]

SPICINESS_CHOICES = [
    ('none', 'None'),
    ('mild', 'Mild'),
    ('medium', 'Medium'),
    ('hot', 'Hot'),
    ('extra_hot', 'Extra Hot'),
]

MEAL_TYPE_CHOICES = [
    ('combo', 'Combo'),
    ('drink', 'Drink'),
    ('main_course', 'Main Course'),
    ('side_dish', 'Side Dish'),
]

FLAVOR_CHOICES = [
    ('sweet', 'Sweet'),
    ('sour', 'Sour'),
    ('umami', 'Umami'),
    ('savory', 'Savory'),
    ('spicy', 'Spicy'),
]

ALLERGEN_CHOICES = [
    ('milk', 'Milk'),
    ('eggs', 'Eggs'),
    ('fish', 'Fish'),
    ('crustacean_shellfish', 'Crustacean Shellfish'),
    ('tree_nuts', 'Tree Nuts'),
    ('peanuts', 'Peanuts'),
    ('wheat', 'Wheat'),
    ('soybeans', 'Soybeans'),
    ('sesame', 'Sesame'),
]

NUTRITION_TAG_CHOICES = [
    ('high_protein', 'High Protein'),
    ('low_carb', 'Low Carb'),
    ('low_sugar', 'Low Sugar'),
    ('low_fat', 'Low Fat'),
    ('high_fiber', 'High Fiber'),
    ('low_calorie', 'Low Calorie'),
]

ALL_TAGS = [
    ("Cuisine", CUISINE_CHOICES),
    ("Protein", PROTEIN_TYPE_CHOICES),
    ("Spiciness", SPICINESS_CHOICES),
    ("MealType", MEAL_TYPE_CHOICES),
    ("Flavor", FLAVOR_CHOICES),
    ("Allergen", ALLERGEN_CHOICES),
    ("Nutrition", NUTRITION_TAG_CHOICES),
]


US_STATE_CHOICES = [
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
]