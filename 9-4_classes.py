
class Restaurant():
    """A restaurant with two attributes"""

    def __init__(self, rname, cstype):
        self.name = rname
        self.type = cstype
        self.number_served = 0

    def describe_restaurant(self):
        print("\nThe restaurant named " + self.name.title()
              + " provides " + self.type)

    def set_number_served(self, num):
        self.number_served = num
        print("The restaurant has served " + str(self.number_served)
              + " people.")

    def increment_number_served(self, newnum):
        self.number_served += newnum
        print("The restaurant has served " + str(self.number_served)
              + " people.")

    def open_restaurant(self):
        print("The restaurant " + self.name.title() + " is open!")


rst = Restaurant('honeymoon', 'italian food')
# opt 1
#rst.number_served = 18
#print(str(rst.number_served) + " customers are served.")

rst.set_number_served(20)
rst.increment_number_served(10)
rst.increment_number_served(100)
