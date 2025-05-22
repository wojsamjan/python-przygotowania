class Circle():
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius


c1 = Circle(10)
print(c1.radius)
# c1.radius = 5
c1._radius = 5
print(c1.radius)
