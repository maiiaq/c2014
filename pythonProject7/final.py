import random


class My_Day:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.alive=True


    def to_wake_up(self):
        print("I woke up")
        self.progress+=5
        self.gladness+=10

    def to_brush_my_teeth(self):
        print("Brushing_my_teeth")
        self.progress += 5
        self.gladness += 5
    def to_heve_a_breackfest(self):
        print("time for eating")
        self.progress+=0.05
        self.gladness+=5
    def to_feed_a_cat(self):
        print("I fed my cat")
        self.progress+=2
        self.gladness+=2
    def to_school_prepairing(self):
        print("time to school prepairing")
        self.progress+=5
        self.gladness-=5
    def to_study(self):
        print("time to study in school")
        self.progress+=20
        self.gladness-=5

    def to_waiting(self):
        print("I need to wait 2 lessons")
        self.gladness-=10
    def to_play_volleyball(self):
        print("do sport")
        self.gladness+=10
        self.progress+=20
    def to_back_home(self):
        print("going to the home")
        self.gladness+=10
    def to_have_a_dinner(self):
        print("Eating dinner")
        self.progress+=2
        self.gladness+=10
    def to_chill(self):
        print("chilling time")
        self.progress-=10
        self.gladness+=20
    def to_play_with_cat(self):
        print("I and my cat were enjoing")
    def to_have_a_supper(self):
        print("Eating a supper")
        self.gladness+=10
    def to_feed_cat(self):
        print("I fed a cat")
        self.progress+=5
        self.gladness+=5
    def to_watch_TV(self):
        print("TV time")
        self.progress -= 10
        self.gladness += 20
    def to_take_a_shower(self):
        print("I was taking shower")
        self.gladness+=5
        self.progress+=5

    def to_brush_my_teeth(self):
        print("Brushing_my_teeth")
        self.progress += 5
        self.gladness += 5

    def to_check_a_social_medias(self):
        print("to watching social medias")
        self.gladness+=10
        self.progress-=5
    def to_sleep(self):
        print("I will sleep")
        self.progress+=5
    def is_alive(self):
        if self.progress<-10:
            print("Bad day")
            self.alive=False
        elif self.gladness<=0:
            print("Depression..")
            self.alive=False
        elif self.progress>10:
            print("Passed extremly")
            self.alive=False
    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress,2)}")
    def live(self,day):
        day="Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube=random.randint(1,3)
        if live_cube==1:
            self.to_study()
        elif live_cube==2:
            self.to_sleep()
        elif live_cube==3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()
class Cat:
    def __init__(self,name):
        self.name=name
        self.gladness=10
        self.alive=True
    def to_eat(self):
        print("I like eating food")
        self.gladness+=10
    def to_play(self):
        print("I am enjoy")
        self.gladness+=10
    def to_sleep(self):
        print("I want to sleep")
        self.gladness+=10
    def to_do_toilet_things(self):
        print("to go to the toilet")
        self.gladness+=5




Maiia=My_Day(name="Maiia")
for day in range(365):
    if Maiia.alive==False:
        break
    Maiia.live(day)