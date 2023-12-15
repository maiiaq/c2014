import random
class Cat:
    def __init__(self,name="Cat", family=None, food=None, room=None):
       self.name=name
       self.cute=100
       self.gladness=50
       self.satiety=50
       self.home=room
       self.food=food
       self.family=family

    def get_home(self):
        self.home=room()
    def get_food(self):
        if self.food():
            pass
        else:
            self.to_find()
            return
    def get_family(self):
        self.family=family(family_list)
    def get_eat(self):
        if self.home.food<=0:
            self.find("food")
        else:
            if self.satiety>=100:
                self.satiety=100
                return
        self.satiety+=5
        self.home.food-=5
    def get_chill(self):
        pass
    def day_indexes(self,day):
        pass
    def is_alive(self):
        pass
    def live(self):
        pass
class family:
    def __init__(self, family_list, ):
        self.count_of_members=random.choice(list(family_list))
        self.daughter=family_list[self.family]["daughter"]
        self.son = family_list[self.family]["son"]
        self.mom = family_list[self.family]["mom"]
class room:
    def __init__(self):
        self.food=0
        self.mess1=0
family_list={
    "standart":{"cat_dad", "cat_mom", "kitten_daughter/son"},
    "big_family":{"cat_dad", "cat_mom", "kitten_daughter", "kitten_son"},
    "large_family":{"cat_dad", "cat_mom", "kitten_son", "kitten_daughter", "kitten_son", "kitten_daughter"},
    "lonely_family":{"cat_dad", "cat_mom"}
}
class food:
    def __init__(self,food_list):
        self.food = random.choice(list(food_list))
        self.salary = food_list[self.food]["salary"]
        self.gladness_less = food_list[self.food]["gladness_less"]

food_list = {
    "fish_fugu": {"salary": 50, "gladness_less": 10},
    "stake": {"salary": 70, "gladness_less": 3},
    "apple": {"salary": 5, "gladness_less": 2},
    "pigeon": {"salary": 20, "gladness_less": 1}
}