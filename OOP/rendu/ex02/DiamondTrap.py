from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    A class representing a King character who inherits traits from both
    the Baratheon and Lannister families.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initialize the King with attributes from Baratheon and\
        Lannister families.

        Args:
            first_name (str): The first name of the King.
            is_alive (bool): The living state of the King.\
            Defaults to True.
        """
        Baratheon.__init__(self, first_name, is_alive)

    def set_eyes(self, color):
        """
        King set_eyes method. Changes eyes attribute
        to the given value.

        Parameters:
            eyes (str): King eyes color.

        Returns:
            None
        """

        try:
            assert isinstance(color, str), \
                "eyes attribute must be a string."

            self.eyes = color

        except AssertionError as e:
            print("AssertionError:", e)

    def set_hairs(self, color):
        """
        King set_hairs method. Changes hairs attribute
        to the given value.

        Parameters:
            hairs (str): King hairs color.

        Returns:
            None
        """
        try:
            assert isinstance(color, str), \
                "hairs attribute must be a string."

            self.hairs = color

        except AssertionError as e:
            print("AssertionError:", e)

    def get_eyes(self):
        """
        King get_eyes method. Returns eyes attribute.

        Parameters:
            None

        Returns:
            str: King eyes color.
        """
        return self.eyes

    def get_hairs(self):
        """
        King get_hairs method. Returns hairs attribute.

        Parameters:
            None

        Returns:
            str: King hairs color.
        """
        return self.hairs
