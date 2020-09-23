from restaurant.chef import Chef


class VeganChef(Chef):

    def __init__(self, name):
        super().__init__(name)

    def make_veg_meal(self):
        print(f"Hey, I'm {self.name}. I can make veg meal")
