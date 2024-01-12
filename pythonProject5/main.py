class WoodError(Exception):
    def __str__(self):
        return f"Нам не вистачає цієї кількості дерева!"
def check_wood(amount_of_wood, limit_value):
    if amount_of_wood>limit_value:
        return " дерева достатньо"
    else:
        raise WoodError(amount_of_wood)
wood=123
check_wood(wood,300)




class EquipmentError(Exception):
    def __str__(self):
        return f"With this count of equipment we can not work !"
def check_equipment(amount_of_equipment, limit_value):
    if amount_of_equipment>limit_value:
        return " the count of equipment is normal to sell"
    else:
        raise EquipmentError(amount_of_equipment)
equipment=123
check_equipment(equipment,200)




class FoodError(Exception):
    def __str__(self):
        return f"With this count of food !"
def check_food(amount_of_food, limit_value):
    if amount_of_food>limit_value:
        return " we have got a many count of food, so we csn sell them"
    else:
        raise FoodError(amount_of_food)
food=123
check_food(food,100)