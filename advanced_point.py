from color_point import ColorPoint  # Import the ColorPoint class from the color_point module

class AdvancedPoint(ColorPoint):  # AdvancedPoint inherits from ColorPoint
    COLORS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"]  # List of valid colors

    def __init__(self, x, y, color):
        # Initialize an AdvancedPoint with x, y, and color
        if color not in self.COLORS:  # Validate the color
            raise TypeError(f"Invalid color, must be one of {self.COLORS}")
        self._x = x  # Store x coordinate
        self._y = y  # Store y coordinate
        self._color = color  # Store color

    @property
    def x(self):
        return self._x  # Getter for x

    @x.setter
    def x(self, value):
        self._x = value  # Setter for x

    @property
    def y(self):
        return self._y  # Getter for y

    @property
    def color(self):
        return self._color  # Getter for color

    @classmethod
    def add_color(cls, color):
        """
        Adds a new valid color to the class-level COLORS list
        """
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color="red"):
        """
        Create a new AdvancedPoint from a tuple (x, y) and a color
        """
        x, y = coordinate  # Unpack the tuple
        return AdvancedPoint(x, y, color)  # Return a new AdvancedPoint

    @staticmethod
    def distance_2_points(p1, p2):
        # Calculate Euclidean distance between two AdvancedPoint objects
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def distance_to_other(self, p):
        # Calculate Euclidean distance from this point to another point p
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

# Example usage:
AdvancedPoint.add_color("rojo")  # Add "rojo" to valid colors
p = AdvancedPoint(1, 2, "rojo")  # Create a point at (1, 2) with color "rojo"
print(p.x)  # Print the x coordinate of p
print(p)  # Print the string representation of p (inherited from ColorPoint or AdvancedPoint)
print(p.distance_orig())  # Call distance_orig() method (likely from ColorPoint, not shown here)
p2 = AdvancedPoint.from_tuple((3, 2))  # Create a new point at (3, 2) with default color "red"
print(p2)  # Print p2
print(AdvancedPoint.distance_2_points(p, p2))  # Print distance between p and p2 using static method
print(p.distance_to_other(p2))  # Print distance between p and p2 using instance method
