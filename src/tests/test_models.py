import pytest
from app.models import User
from app.utils.exceptions import InvalidDataError


def test_user_creation_valid_name():
    """
    Test the User creation with a valid name.

    Ensures that a User object is correctly created with a valid
    name and the name attribute is properly assigned.
    """

    # Arrange
    user_id = 1
    valid_name = "pepe perez"
    created_at = "2024-07-24 08:00:00"

    # Act
    user = User(user_id, valid_name, created_at)

    # Assert
    assert user.name == valid_name


def test_user_creation_sql_injection():
    """
    Test the User creation with a name containing SQL injection characters.

    Ensures that an `InvalidDataError` is raised when an attempt
    create a User with a name that includes SQL injection characters.
    """

    # Arrange
    user_id = 1
    created_at = "2024-07-24 08:00:00"
    invalid_name = 'Pepito"; DROP TABLE users;--'

    # Act and Assert
    with pytest.raises(InvalidDataError, match="Invalid data provided."):
        User(user_id, invalid_name, created_at)


def test_user_creation_empty_name():
    """
    Test the User creation with an empty name.

    Ensures that an InvalidDataError is raised when trying to
    create a User object with an empty name, which is an invalid input.
    """

    # Arrange
    user_id = 1
    empty_name = ""
    created_at = "2024-07-24 08:00:00"

    # Act and Assert
    with pytest.raises(InvalidDataError, match="Invalid data provided."):
        User(user_id, empty_name, created_at)
