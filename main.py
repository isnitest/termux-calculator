def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def divi(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def modulo(a, b):
    if b == 0:
        return "Error"
    return a % b

if __name__ == "__main__":
    x = float(input("Enter first number (x): "))
    y = float(input("Enter second number (y): "))
    print()
    
    print(f"Addition ({x} + {y}) = {add(x, y)}")
    print(f"Subtraction ({x} - {y}) = {sub(x, y)}")
    print(f"Multiplication ({x} * {y}) = {mult(x, y)}")
    print(f"Division ({x} / {y}) = {divi(x, y)}")
    print(f"Modulo ({x} % {y}) = {modulo(x, y)}")

