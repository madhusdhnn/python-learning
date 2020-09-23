from restaurant.chef import Chef


class NonVeganChef(Chef):

    def __init__(self, name):
        super().__init__(name)

    def make_bbq(self):
        print(f"Hey, I'm {self.name}. I can make BBQ chicken")
