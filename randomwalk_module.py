from random import choice

class RandomWalk:
    '''a class to generate random walks'''
    def __init__(self, num_points = 5000):
        '''initialize the random walk'''
        self.num_points = num_points
        
        # starting point at (0,0)
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        '''calculate each point as a step in our walk'''
        # keep taking steps until it reaches the max number
        while len(self.x_values) < self.num_points:
            # process of defining the direction and length of each step
            x_step = self.get_step()
            y_step = self.get_step()
            
            # ignore no movements steps
            if y_step == 0 and x_step == 0:
                continue
            
            # calculate new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)
        
    def get_step(self,distance_rang = 6):
        self.distance_range = distance_rang
        direction = choice([-1,1])
        distance = choice(list(range(self.distance_range)))
        step = direction * distance
        return step
        