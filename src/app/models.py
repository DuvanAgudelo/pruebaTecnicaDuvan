import logging
from app.utils.patterns import NAME_PATTERN
from app.utils.exceptions import InvalidDataError
from datetime import datetime
import re


class User:
    """
    Represents a user with validation and serialization.

    This class defines a user with attributes such as `id`, `name`, and `created_at`.
    It includes validation for the user name and a method to serialize the user data
    into a JSON-compatible format.
    """

    def __init__(self, id, name, created_at=None):
        """
        Initializes a User instance with the given attributes and validates the user data.

        Args:
            id: The unique identifier for the user.
            name: The name of the user.
            created_at: The timestamp when the user was created.

        Raises:
            InvalidDataError: If the name does not match the required pattern.
        """
        self.id = id
        self.name = name
        self.created_at = self.get_timestamp(created_at)
        self.validate()

    def get_timestamp(self, timestamp):
        """
        Returns the provided timestamp or the current time if no timestamp is provided.

        Args:
            timestamp: The provided timestamp.

        Returns:
            The timestamp in 'YYYY-MM-DD HH:MM:SS' format.
        """

        return timestamp or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def validate(self):
        """
        Validates the user's name against the predefined pattern.

        Raises:
            InvalidDataError: If the name does not match the required pattern.
        """
        if not self.name or not re.match(NAME_PATTERN, self.name):
            logging.error("error in the name: %s", str(self.name))
            raise InvalidDataError()

    def to_json(self):
        """
        Converts the User object to a JSON-serializable dictionary.

        Returns:
            dict: The User object in JSON format.
        """
        return {"id": self.id, "name": self.name, "created_at": self.created_at}
