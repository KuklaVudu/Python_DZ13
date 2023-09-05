# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
# Напишите к ним классы исключения с выводом подробной информации. 
# Поднимайте исключения внутри основного кода. 
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.
from MyException import NegativeError, TreagleError


class Treagle:
    def __init__(self, A: int, B: int, C: int) -> None:
        if A > 0:
            self.A = A
        else:
            raise NegativeError(A, 0)
        if B > 0:
            self.B = B
        else:
            raise NegativeError(B, 0)
        if C > 0:
            self.C = C
        else:
            raise NegativeError(C, 0)
        
    def compare(self):
        if (self.A + self.B < self.C or self.A + self.C < self.B or self.B + self.C < self.A):
            raise TreagleError(self.A, self.B, self.C)
        else:
            if (self.A == self.B and self.B == self.C and self.C == self.A):
                return 'Треугольник равносторонний'
            elif (self.A != self.B and self.B != self.C):
                return 'Треугольник разносторонний.'  
            else:
                return 'Треугольник равнобедренный.'  

if __name__ == "__main__":   
    try:
        A = -9
        B = 5
        C = 4
    except Exception as number:
        raise ValueError(f"Формат ввода только цифры: {number}")

    r1 = Treagle(A, B, C)
    print(r1.compare())   