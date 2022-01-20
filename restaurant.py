class Restaurant():
    """A restaurant with two attributes"""

    def __init__(self, rname, cstype):
        self.name = rname
        self.type = cstype

    def describe_restaurant(self):
        print("\nThe restaurant named " + self.name.title()
              + " provides " + self.type)


class IceCreamStand(Restaurant):
    def __init__(self, rname, cstype):
        super().__init__(rname, cstype)
        self.flavors = ['chocolate', 'coconut', 'vanilla']

    def display_flavors(self):
        print("Would you like some ice cream of: ")
        for flavor in self.flavors:
            print('- ' + flavor.title())