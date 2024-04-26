class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print(f"Hi..  my name is {self.name}. \nMy color is {self.color}. \nMy weight is {self.weight}.")

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

class Person:
    def __init__(self, name, personality, is_sitting):
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False 

p1 = Person("Ali", "aggressive", False)
p2 = Person("Hamza", "talkative", True)

p1.robot_owned = r2  # p1 owns r2
p2.robot_owned = r1  # p2 owns r1

p1.robot_owned.introduce_self()
p2.robot_owned.introduce_self()
        