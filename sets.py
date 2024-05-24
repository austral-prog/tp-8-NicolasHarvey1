from sets_categories_data import (ALCOHOLS)

def clean_ingredients(dish_name, dish_ingredients):
    unique_ingredients = set(dish_ingredients)
    return dish_name, unique_ingredients

def check_drinks(drink_name, drink_ingredients):
    for i in drink_ingredients:
        if i in ALCOHOLS:
            return drink_name + " Cocktail"
    return drink_name + " Mocktail"
