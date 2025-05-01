import random  # Import random module for generating random values
from ftplib import parse227  # Import parse227 function from ftplib (not used in this code)


class Point:
    """
    Class modeling a real life 2D point
    """
    def __init__(self, x, y):
        """
        Initialize the point instance
        :param x: the x axis coordinate value
        :param y: the y axis coordinate value
        """
        self.x = x  # Set x coordinate
        self.y = y  # Set y coordinate

    def __str__(self):
        # Define string representation of a Point
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        # Define representation, uses __str__ for consistency
        return self.__str__()

    def distance_orig(self):
        # Calculate Euclidean distance from origin (0,0)
        return (self.x**2 + self.y**2)**0.5

    def __gt__(self, other):
        """
        Magic method that is called when you do self>other
        :param other: the other point comparing against
        :return: True/False
        """
        # Compare points based on their distance from origin
        return self.distance_orig() > other.distance_orig()

    def __eq__(self, other):
        # Check equality based on distance from origin
        return self.distance_orig() == other.distance_orig()

if __name__ == "__main__":
    points = []  # Initialize empty list to store points
    for i in range(5):
        # create a random point
        p = Point(
            random.randint(-100, 100),  # Random x between -100 and 100
            random.randint(-100, 100)   # Random y between -100 and 100
        )
        # append it to the list
        points.append(p)

    print("unsorted points")  # Print header for unsorted points
    print(points)  # Print list of random points
    print("sorted points")  # Print header for sorted points
    points.sort()  # Sort points by distance from origin (uses __gt__ method)
    print(points)  # Print sorted points

    found_equal = 0  # Counter for points with equal distances from origin
    count = 0  # Counter for total point pairs compared
    while True:
        if found_equal == 10000:  # Stop after finding 10,000 equal pairs
            break
        p1 = Point(
            random.randint(-100, 100),  # Generate random point 1
            random.randint(-100, 100)
        )
        p2 = Point(
            random.randint(-100, 100),  # Generate random point 2
            random.randint(-100, 100)
        )
        count += 1  # Increment total pairs count
        if p1 == p2:  # Check if distances from origin are equal
            # print(p1, p2)
            found_equal += 1  # Increment equal pairs count

    print(f"probability is 1 in {count/found_equal} ")  # Print the probability ratio
