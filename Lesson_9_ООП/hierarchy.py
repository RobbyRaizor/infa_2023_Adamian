class Base:
    def __init__(self, x):
        self.x = x

    def show(self):
        print('Base', self.x)


class Derivative(Base):
    def __init__(self):
        Base.__init__(self, 24) #явное обращение к род. классу. Когда несколько род. классов, то только так.
        super().__init__(40) #обращение к род. классу через супер. Не нужно селф использовать
        self.name = ''


a = Base(12)
a.show()

b = Derivative()
b.show()
