
class Restaurant():
    """A restaurant with two attributes"""

    def __init__(self, rname, cstype):
        self.name = rname
        self.type = cstype

    def describe_restaurant(self):
        print("\nThe restaurant named " + self.name.title() +
              " provides " + self.type)

    def open_restaurant(self):
        print("The restaurant " + self.name.title() + " is open!")


rst = Restaurant('honeymoon', 'italian food')
# rst.describe_restaurant()
# rst.open_restaurant()

rst1 = Restaurant('black chocolate', 'sweets')
rst1.describe_restaurant()
