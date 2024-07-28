import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k in kwargs:
            self.contents.extend(k for _ in range(kwargs[k]))
        self.__initial_contents = copy.deepcopy(self.contents)

    def reset(self):
        self.contents = copy.deepcopy(self.__initial_contents)

    def draw(self, number_of_ball):
        if number_of_ball > len(self.contents):
            drawed_balls = copy.deepcopy(self.contents)
            self.contents = []
            return drawed_balls
            
        drawed_balls = []
        for _ in range(number_of_ball):
            ball = random.choice(self.contents)
            drawed_balls.append(ball)
            self.contents.remove(ball)
        
        return drawed_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_correct = 0

    for _ in range(num_experiments):
        drawed_balls_list = hat.draw(num_balls_drawn)
        hat.reset()

        drawn_dict = {ball: drawed_balls_list.count(ball) for ball in drawed_balls_list}
        list_check = [drawn_dict[key] >= expected_balls[key] if key in drawn_dict else False for key in expected_balls]
        if all(list_check):
            num_correct += 1
        

    return num_correct / num_experiments

hat1 = Hat(black=6, red=4, green=3)
print(experiment(hat=hat1,expected_balls={'red':2,'green':1}, num_balls_drawn=5, num_experiments=2000))