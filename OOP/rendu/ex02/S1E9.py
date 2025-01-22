from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character."""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Constructor for Character.
        Args:
            first_name(str): The first name of the charactor.
            is_alive (bool, optional): The living state of the character
            . Defaults to True.
        """
        try:
            assert isinstance(first_name, str), \
                "first_name must be string"
            assert isinstance(is_alive, bool), \
                "is_alive must be boolean"

            self.first_name = first_name
            self.is_alive = is_alive

        except AssertionError as e:
            print("AssertionError:", e)

    def die(self):
        """Changes the character's state to dead."""
        self.is_alive = False


class Stark(Character):
    """Class representing a Stark character."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Stark.
        Args:
            first_name (str): The first nam of the Stark character.
            is_alive (bool): The living state of the character.
            Default to True.
        """
        super().__init__(first_name, is_alive)
