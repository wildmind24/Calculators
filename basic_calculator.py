import math

# All possible operations are included in Operation class
class Operation:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    @staticmethod
    def power(a):
        return a*a

    @staticmethod
    def square_root(a):
        if a < 0:
            raise ValueError("Cannot compute the square root of a negative number.")
        return math.sqrt(a)

    @staticmethod
    def modulus(a, b):
        return a % b


# For saving/adding to history, a History class
class History:
    def __init__(self):
        self.history = []

    def add_to_history(self, operation, result):
        self.history.append(f"{operation} = {result}")

    def show_history(self, count=5):
        return self.history[-count:]


# Calculator Class to call static methods/ Basic Operations
class Calculator:
    def __init__(self):
        self.history = History()

    def calculate(self, operation, a, b=None):
        try:
            if operation == "add":
                result = Operation.add(a, b)
            elif operation == "subtract":
                result = Operation.subtract(a, b)
            elif operation == "multiply":
                result = Operation.multiply(a, b)
            elif operation == "divide":
                result = Operation.divide(a, b)
            elif operation == "power":
                result = Operation.power(a)
            elif operation == "modulus":
                result = Operation.modulus(a, b)
            elif operation == "sqrt":
                result = Operation.square_root(a)
            else:
                raise ValueError("Invalid operation.")
     
            
                   
                                 
            # add calculator operation to history
            operation_desc = f"{operation}({a}, {b})" if b is not None else f"{operation}({a})"
            self.history.add_to_history(operation_desc, result)
            
            return result
        except Exception as e:
            return f"Error: {str(e)}"

    def show_history(self, count=5):
        return self.history.show_history(count)






# Main Program to run on CLI
def main():
    calculator = Calculator()
    print("Welcome to the Basic Calculator System!")

    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Modulus")
        print("8. Show History")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "9":
            print("Thank you for using the calculator!")
            break
        
        if choice in {"1", "2", "3", "4", "7"}:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                continue
        elif choice == "5":
            try:
                a = float(input("Enter the number: "))
                b = None
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
                continue
        elif choice == "6":
            try:
                a = float(input("Enter the number: "))
                b = None
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
                continue
        elif choice == "8":
            try:
                count = int(input("How many recent operations to show? "))
                history = calculator.show_history(count)
                print("\nHistory:")
                for item in history:
                    print(item)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            continue
        else:
            print("Invalid choice! Try again.")
            continue

# To link choice to operation
        operation_map = {
            "1": "add",
            "2": "subtract",
            "3": "multiply",
            "4": "divide",
            "5": "power",
            "6": "sqrt",
            "7": "modulus"
        }

        operation = operation_map.get(choice)
        result = calculator.calculate(operation, a, b)
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
    
    
    
    