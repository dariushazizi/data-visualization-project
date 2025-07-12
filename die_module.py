class Die:
    "creating a class for die rolling"
    def __init__(self,sides = 6):
        self.sides = sides
        self.num_range = list(range(1,sides+1))
        
    def set_sides(self,new_sides):
        self.sides = new_sides
        
    def increase_sides(self, added_sides):
        self.sides += added_sides
        
    def range_change(self, begin_num, end_num):
        if (end_num - begin_num +1) != self.sides:
            print('the range is lower than sides!')
        else:
            self.num_range = range(begin_num,end_num)
        
    def roll_die(self,roll_number):
        from random import choice
        print(f'\nthe {self.sides} sided die showed the numbers below:')
        for turn in range(roll_number):
            result = choice(self.num_range)
            print(f'-{turn+1} num is: {result}')
            
    def roll(self,roll_number):
        self.rolls_number = roll_number
        from random import choice
        result_list = []
        for turn in range(roll_number):
            result = choice(self.num_range)
            result_list.append(result)
        return result_list