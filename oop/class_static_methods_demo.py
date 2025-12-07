# class_static_methods_demo.py

class Calculator:
    """
    A simple Calculator class demonstrating the difference
    between static methods and class methods.
    """

    # Class attribute shared by all instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method:
        - Does not use the class or instance (no self or cls)
        - Behaves like a normal function grouped inside the class for organization
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method:
        - Receives the class itself as 'cls'
        - Can access class attributes (like calculation_type)
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
