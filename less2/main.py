import random
class Human:
    def __init__(self,name="Human", car=None, job=None, home=None, pet=None):
       self.name=name
       self.money=100
       self.gladness=50
       self.satiety=50
       self.home=home
       self.job=job
       self.car=car
       self.pet=pet
    def get_pet(self):
        if self.money>=10:
            self.money-=5
            self.gladness+=10
            self.pet = Pet(kind_of_pet)
        else:
            self.gladness-=10
            pass
    def get_home(self):
        self.home=House()
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job=Job(job_list)
    def get_car(self):
        self.car=Auto(brand_of_car)
    def get_eat(self):
        if self.home.food<=0:
            self.get_shopping("food")
        else:
            if self.satiety>=100:
                self.satiety=100
                return
        self.satiety+=5
        self.home.food-=5
    def get_work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel<20:
                self.get_shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money+=self.job.salalry()
        self.gladness+=self.job.gladness_less()
        self.satiety-=4
    def get_shopping(self,manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel<20:
                self.get_shopping("fuel")
                return
            else:
                self.to_repair()
                return
        if manage=="fuel":
            print("I bought fuel")
            self.money-=100
            self.car.fuel+=100
        elif manage=="food":
            print("i bought food")
            self.money-=50
            self.home.food+=50
        elif manage=="delicacias":
            print("i bought delicacias")
            self.gladness+=10
            self.satiety+=2
            self.money-=50
    def get_chill(self):
        self.gladness+=10
        self.home.mess+=5
    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
    def to_repair(self):
        self.car.strength+=100
        self.money-=50


    def day_indexes(self,day):
        day=f"Today the{day} of {self.name}`s life"
        print(f"{day:=^50}","\n")
        human_indexes=self.name + "'s indexes"
        print(f"{human_indexes:^50}","\n")
        print(f"Money-{self.money}")
        print(f"Gladness - {self.gladness}")
        print(f"Satiety - {self.satiety}")
        home_indexes="Home indexes"
        print(f"{home_indexes:=^50}", "\n")
        print(f"Food-{self.home.food}")
        print(f"Mess-{self.home.mess}")
        car_indexes=f"{self.car.brand} car.indexes"
        print(f"{car_indexes:=^50}", "\n")
        print(f"Fuel-{self.car.fuel}")
        print(f"strength-{self.car.strength}")


    def is_alive(self):
        if self.gladness<0:
            print("Depresion")
            return False
        if self.satiety<0:
            print("Dead")
            return False
        if self.money<-500:
            print("Bankrupt")
            return False


    def live(self,day):
        if self.is_alive()==False:
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"i bought a car{self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"i don`t have job, i am going to get it{self.job.job} with salary{self.job.salary}")
            self.day_indexes(day)
        dice=random.randint(1,4)
        if self.satiety<20:
            print("i will go to eat")
            self.get_eat()
        elif self.gladness<20:
            if self.home.mess<15:
                print("I want to chill, but there is so much mess…\n So I will clean the house")
                self.clean_home()
            else:
                print(" let`s chill")
                self.get_chill()
        elif self.money<0:
            print("start work")
            self.get_work()
        elif self.car.strength <15:
            print("i need to repair my car")
            self.to_repair()
        elif dice==1:
            print("let`s chill")
            self.get_chill()
        elif dice==2:
            print("start working")
            self.get_work()
        elif dice==3:
            print("let`s cleaning")
            self.get_work()
        elif dice == 4:
            print("time for treats")
            self.get_shopping(manage="delicacias")

class Auto:
    def __init__(self, brand_list):
        self.brand=random.choice(list(brand_list))
        self.fuel=brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]
    def drive(self):
        if self.strength>0 and self.fuel>self.consumption:
            self.fuel=self.consumption
            self.strength-=1
            return True
        else:
            print("the car can not move")
            return False

class Pet:
    def __init__(self, pet_list):
        self.pet=random.choice(list(pet_list))
        self.kind=pet_list[self.pet]["kind"]
        self.age = pet_list[self.pet]["age"]
class House:
    def __init__(self):
        self.food=0
        self.mess=0
brand_of_car={
    "BMW":{"fuel":100, "strength":100, "consumption":12},
    "toyota":{"fuel":50, "strength":60, "consumption":10},
    "volvo":{"fuel":70, "strength":120, "consumption":8},
    "porsche":{"fuel":800, "strength":150, "consumption":14}
}
job_list={
    "Java developer":{"salary":50, "gladness_less":10},
    "c++ developer":{"salary":40, "gladness_less":3},
    "python developer":{"salary":45, "gladness_less":25},
    "rust developer":{"salary":70, "gladness_less":1}
}
kind_of_pet={
    "dog":{"age":20},
    "fish":{"age":5},
    "hamster":{"age":3},
    "cat":{"age":20}
}


class Job:
    def __init__(self,job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]
nick=Human(name="nick")
for day in range(1,8):
    if nick.live(day)==False:
        break
