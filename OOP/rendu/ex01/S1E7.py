from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """
        Baratheon constructor method. Initializes first_name,
        is_alive, family_name, eyes and hairs attributes.

        Parameters:
            first_name (str): Baratheon first name.
            is_alive (bool): Baratheon status. Optional. Default is True.
        """

        try:
            assert isinstance(first_name, str), \
                "first_name must be string"
            assert isinstance(is_alive, bool), \
                "is_alive must be bool"

            self.first_name = first_name
            self.is_alive = is_alive
            self.family_name = "Baratheon"
            self.eyes = "brown"
            self.hairs = "dark"

        except AssertionError as e:
            print("AssertionError:", e)

    def __str__(self):
        """Return a descriptive string for the Barathorn character."""
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self):
        """Return a string representation of the Barathoen character."""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Lannester character with default attributes."""
        try:
            assert isinstance(first_name, str), \
                "first_name must be string"
            assert isinstance(is_alive, bool), \
                "is_alive must be bool"

            self.first_name = first_name
            self.is_alive = is_alive
            self.family_name = "Lannister"
            self.eyes = "blue"
            self.hairs = "light"

        except AssertionError as e:
            print("AssertionError:", e)

    def __str__(self):
        """Return a description string for the Lannister character."""
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self):
        """Return a string representation of the Lannister character"""
        return self.__str__()

    @classmethod
    def create_lannister(self, first_name, is_alive=True):
        """Create a new Lannister character."""
        return Lannister(first_name, is_alive)
