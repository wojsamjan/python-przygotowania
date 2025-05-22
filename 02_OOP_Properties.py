class Circle():
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """The radius property"""
        print('Get radius')
        return self._radius

    @radius.setter
    def radius(self, value):
        print('Set radius')
        self._radius = value

    @radius.deleter
    def radius(self):
        print('Delete radius')
        del self._radius


c1 = Circle(10)
print(c1.radius)
c1.radius = 5
print(c1.radius)
del c1.radius
print(c1.radius)
