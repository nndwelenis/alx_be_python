# Define the Student class
class Student:
    # Constructor method that runs when you create a new Student object
    def __init__(self, name, age):
        self.name = name      # Store the student's name
        self.age = age        # Store the student's age

    # Method to display information about the student
    def get_descriptive_name(self):
        print(f"I am {self.name} and my age is {self.age}")


# Create an object (instance) of the Student class
student1 = Student("John", 18)

# Call the method to display the student's information
student1.get_descriptive_name()
