import random


class Puppy:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.alive=True

    def to_play(self):
        print("time to play")
        self.progress+=1
        self.gladness+=5
    def to_sleep(self):
        print("I will sleep")
        self.progress+=5
    def to_eat(self):
        print("eat time")
        self.progress-=0.1
        self.gladness+=5
    def is_alive(self):
        if self.progress<-0.5:
            print("throw it on the street")
            self.alive=False
        elif self.gladness<=0:
            print("sad..")
            self.alive=False
        elif self.progress>5:
            print("stay at home")
            self.alive=False
    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress,2)}")
    def live(self,day):
        day="Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube=random.randint(1,3)
        if live_cube==1:
            self.to_play()
        elif live_cube==2:
            self.to_sleep()
        elif live_cube==3:
            self.to_eat()
            self.end_of_day()
            self.is_alive()
Martin=Puppy("name=Martin")
for day in range(365):
    if Martin.alive==False:
        break
    Martin.live(day)