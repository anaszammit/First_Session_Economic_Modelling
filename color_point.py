from point import Point  # Import the Point class from the point module
import random  # Import random module for generating random values

class ColorPoint(Point):  # Define ColorPoint class inheriting from Point
    def __init__(self, x, y, color):
        """
        Defines a color point x, y, color
        """
        self.x = x  # Set x coordinate
        self.y = y  # Set y coordinate
        self.color = color  # Set color attribute

    def __str__(self):
        # Define string representation of ColorPoint
        return f"<{self.x},{self.y}>({self.color})"

color_points = []  # Initialize empty list to store ColorPoint objects
colors = ["red", "blue", "green", "yellow", "black", "white", "purple"]  # Define list of possible colors

for _ in range(5):  # Create 5 random color points
    p = ColorPoint(
        random.randint(-100, 100),  # Random x between -100 and 100
        random.randint(-100, 100),  # Random y between -100 and 100
        random.choice(colors))  # Random color from the colors list
    color_points.append(p)  # Add the point to our list

print("random color points:")  # Print header
print(color_points)  # Print the list of random points

color_points.sort()  # Sort the points (uses comparison from parent Point class)
print("color points in order:")  # Print header
print(color_points)  # Print the sorted points
