class SimpleCalculator:
    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the quotient of a and b. Raises an error if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def show_menu(self):
        """Display the calculator menu options."""
        print("Simple Calculator")
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

    def get_user_choice(self):
        """Get the user's choice of operation."""
        choice = input("Enter choice (1/2/3/4/5): ")
        return choice

    def get_numbers(self):
        """Prompt the user to enter two numbers."""
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b

    def run(self):
        """Run the calculator until the user decides to exit."""
        while True:
            self.show_menu()
            choice = self.get_user_choice()

            if choice == '5':
                print("Exiting the calculator. Goodbye!")
                break

            if choice in ['1', '2', '3', '4']:
                a, b = self.get_numbers()

                if choice == '1':
                    print(f"Result: {self.add(a, b)}")
                elif choice == '2':
                    print(f"Result: {self.subtract(a, b)}")
                elif choice == '3':
                    print(f"Result: {self.multiply(a, b)}")
                elif choice == '4':
                    try:
                        print(f"Result: {self.divide(a, b)}")
                    except ValueError as e:
                        print(e)
            else:
                print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    # Create a calculator instance and run it
    calculator = SimpleCalculator()
    calculator.run()