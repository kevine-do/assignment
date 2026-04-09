def calculator(a, b, operation):

    match operation:
        case "add":
            return a + b

        case "subtract" :
            return a - b

        case "multiply" :
            return a * b

        case "divide" :
            if b == 0:
                return "Error"
            return a / b

        case _:
            return "Invalid operation"



a = float(input("Enter number a: "))
b = float(input("Enter number b: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

result = calculator(a, b, operation)
print("Result:", result)