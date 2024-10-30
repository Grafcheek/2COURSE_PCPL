#объектно-ориентированная парадигма
import math

class BiquadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    @staticmethod
    def input_coefficient(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите число.")

    @staticmethod
    def format_root(root):
        if root.is_integer():
            return str(int(root))
        return str(root)

    def solve(self):
        if self.a == 0:
            print("Коэффициент A не может быть равен 0.")
            return
        
        discriminant = self.b**2 - 4 * self.a * self.c
        print(f"Дискриминант: {discriminant}")
        
        if discriminant < 0:
            print("Действительных корней нет.")
            return
        
        sqrt_discriminant = math.sqrt(discriminant)
        y1 = (-self.b + sqrt_discriminant) / (2 * self.a)
        y2 = (-self.b - sqrt_discriminant) / (2 * self.a)
        
        roots = []
        if y1 >= 0:
            roots.append(math.sqrt(y1))
            roots.append(-math.sqrt(y1))
        if y2 >= 0 and y2 != y1:
            roots.append(math.sqrt(y2))
            roots.append(-math.sqrt(y2))
        
        if roots:
            formatted_roots = [self.format_root(r) for r in sorted(set(roots))]
            print(f"Действительные корни: [{'; '.join(formatted_roots)}]")
        else:
            print("Действительных корней нет.")

def main():
    print("Объщий вид уравнения: Ax^4 + Bx^2 + C= 0")
    a = BiquadraticEquation.input_coefficient("Введите коэффициент A: ")
    b = BiquadraticEquation.input_coefficient("Введите коэффициент B: ")
    c = BiquadraticEquation.input_coefficient("Введите коэффициент C: ")
    
    equation = BiquadraticEquation(a, b, c)
    equation.solve()
    print("ООП")

if __name__ == "__main__":
    main()
