class Series:
    """
    A class to represent a Series, a one-dimensional column (array) with a name.
    """

    def __init__(self, data: list[float], name: str):
        """
        Initialize the Series with data and a name.

        :param data: A list of numerical data.
        :param name: The name of the series (e.g., column name).
        """
        self.data = data
        self.name = name


    def __repr__(self) -> str:
        """Return a string representation of the Series."""
        return f"Series(name={self.name}, data={self.data})"


    def sum(self) -> float:
        """Return the sum of the data in the series."""
        # TODO: Person 3 - Implement this function


    def max(self) -> float:
        """Return the maximum value in the series."""
        # TODO: Person 4 - Implement this function


    def min(self) -> float:
        """Return the minimum value in the series."""
        # TODO: Person 3 - Implement this function


    def mean(self) -> float:
        """Return the mean of the data in the series."""
        # TODO: Person 4 - Implement this function


    def apply(self, func):
        """
        Apply a mapping function to each element in the series and return a new Series.

        :param func: A function to apply to each element.
        :return: A new Series with the function applied.
        """
        # TODO: Person 3 - Implement this function
    
    