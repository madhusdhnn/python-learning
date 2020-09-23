from restaurant.chef import Chef


class MultiCuisineChef(Chef):

    def __init__(self, name):
        super().__init__(name)

    def make_chicken(self):
        print(f"Hey, I'm {self.name}. I can make chicken")

    def make_veg_burger(self):
        print(f"Hey, I'm {self.name}. I can make veg burger")
