# pattern_drawing.py

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for rows
while row < size:
    # Use a for loop to print stars in each row
    for i in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
