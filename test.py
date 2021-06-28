class Person:

    def __init__(self, name, job, money = 0):

        self.name = name
        self.job = job
        self.money = money

    def z_p(self, percent):

        self.money = self.money * (1 + percent)


    def __str__(self):

        return f'Сотрудник с именем {self.name} стоящий на должности {self.job} \n \
            получит заработную плату  в размере {self.money}'


class Manager(Person):

    def __init__(self, name, job, money):
        Person.__init__(self, name,  'Manager', money)

    def z_p(self, percent, bonus = 0.2):

        super().z_p(percent + bonus)


bob = Manager('Артем Самойленко', 'Ingener', 10000)
bob.z_p(0.2)
jon = Person('Александр Теслюк', 'Ingener' , 10000)
jon.z_p(0.2)
print(bob)
print(jon)

