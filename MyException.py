class MyExceptions(Exception):
    pass

class TreagleError(MyExceptions):  
    def __init__(self, A: int, B: int, C: int):
        self.A = A
        self.B = B
        self.C = C
    
    def __str__(self):
        return f'Tреугольника с такими сторонами {self.A}, {self.B}, {self.C} не существует!'

    
class NegativeError(MyExceptions):
    def __init__(self, param, value):
        self.param = param
        self.value = value
    
    def __str__(self):
        if self.param < self.value:
            return f'Нельзя создавать треугольник со сторонами отрицательной длины\n' \
            f'{self.param} < {self.value}'
        elif self.param == self.value:
            return f'Нельзя создавать треугольник сторона которого равна нулю\n' \
            f'{self.param} = {self.value}'