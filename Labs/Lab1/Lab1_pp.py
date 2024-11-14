#процедурная парадигма
import sys
import math

def input_coefficient(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

def format_root(root):
    # Проверяем, является ли число целым
    if root.is_integer():
        return str(int(root))
    return str(root)

def solve_biquadratic(a, b, c):
    if a == 0:
        print("Коэффициент A не может быть равен 0.")
        return
    
    discriminant = b**2 - 4*a*c
    print(f"Дискриминант: {discriminant}")
    
    if discriminant < 0:
        print("Действительных корней нет.")
        return
    
    sqrt_discriminant = math.sqrt(discriminant)
    y1 = (-b + sqrt_discriminant) / (2 * a)
    y2 = (-b - sqrt_discriminant) / (2 * a)
    
    roots = []
    if y1 >= 0:
        roots.append(math.sqrt(y1))
        roots.append(-math.sqrt(y1))
    if y2 >= 0 and y2 != y1:
        roots.append(math.sqrt(y2))
        roots.append(-math.sqrt(y2))
    
    if roots:
        roots = sorted(set(roots))
        formatted_roots = [format_root(r) for r in roots]
        print(f"Действительные корни: [{'; '.join(formatted_roots)}]")
    else:
        print("Действительных корней нет.")

def get_coefficients():
    coefficients = []
    prompts = ["A", "B", "C"]
    
    for i in range(1, 4):
        if len(sys.argv) > i:
            try:
                coefficients.append(float(sys.argv[i]))
            except ValueError:
                print(f"Некорректный коэффициент {prompts[i-1]} в командной строке. Введите его вручную.")
                coefficients.append(input_coefficient(f"Введите коэффициент {prompts[i-1]}: "))
        else:
            coefficients.append(input_coefficient(f"Введите коэффициент {prompts[i-1]}: "))
    
    return coefficients

if __name__ == "__main__":
    print("Объщий вид уравнения: Ax^4 + Bx^2 + C = 0")
    a, b, c = get_coefficients()
    solve_biquadratic(a, b, c)
    print("ПП")
