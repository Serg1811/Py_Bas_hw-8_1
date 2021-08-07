from pprint import pprint
def get_shop_list_by_dishes(dishes, person_count):
    shop_list ={}
    for dish in dishes:
        try:
            for ingredient_dish in cook_book[dish]:
                # print(ingredient_dish)
                ingredient_dish_shop = ingredient_dish.copy()
                ingredient_dish_shop['quantity'] *= person_count
                ingredient_name = ingredient_dish_shop.pop('ingredient_name')
                # print(ingredient_dish)
                # ingredient_quantity = {x:z for x, y in ingredient_dish.items() if x == 'quantity': z = person_count * y elif x != 'ingredient_name': z = y}
                ingredient = shop_list.setdefault(ingredient_name, ingredient_dish_shop)
                # print(shop_list)
                if ingredient != ingredient_dish_shop:
                    ingredient['quantity'] += person_count*ingredient_dish_shop['quantity']
                    shop_list[ingredient_name] = ingredient
        except:
            print (f'в книге нет блюда"{dish}"')
    return shop_list

cook_book = {}
# ingredients = []
# dishes
with open('recipes.txt', encoding='utf-8') as f:
    # print(f.readlines())
    for line in f:
        dish = line.strip()
        quantity_ingredients = int(f.readline().strip())
        ingredients = []
        for number_ingredient in range(quantity_ingredients):
            ingredient = {}
            # print(number_ingredient)
            name, quantity, measure = f.readline().strip().split('|')
            ingredient['ingredient_name'] = name
            ingredient['quantity'] = int(quantity)
            ingredient['measure'] = measure
            ingredients.append(ingredient)
        f.readline()
        cook_book[dish] = ingredients
pprint(cook_book)

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Утка по-пекински'], 2))
