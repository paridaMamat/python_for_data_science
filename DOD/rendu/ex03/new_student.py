import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Represents a student.

    Attributes:
        name (str): The name of the student.
        surname (str): The surname of the student.
        active (bool): Indicates if the student is active. Default is True.
        login (str): The login of the student.
        id (str): The ID of the student.

    Methods:
        __post_init__(self): Initializes the login attribute and
        the id attribute.
    """
    name: str
    surname: str
    active: bool = field(default=True, init=False)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """
        Initializes the login and the id attribute.
        """
        try:
            if not self.name:
                raise ValueError("Error: Name must be a non-empty string")
            if not self.surname:
                raise ValueError("Error: Surname must be a non-empty string")

            # Initialize login and ID after validation
            self.login = f"{self.name[0].upper()}{self.surname.lower()}"
            self.id = generate_id()

        except AssertionError as e:
            print(f"Error initializing Student: {e}")
