from app.repository import UserRepository
from app.models import User


class UserService:
    """
    Service class for handling user-related operations.

    This class provides a layer of abstraction between the application's business logic
    and the data access layer. It interacts with the `UserRepository` to perform operations
    such as retrieving and creating users.

    Attributes:
        repository: An instance of the `UserRepository` class that
                                      provides methods for accessing user data.
    """

    def __init__(self, repository: UserRepository):
        """
        Initializes the UserService with a repository instance.

        Args:
            repository: An instance of the `UserRepository` class
                                          used for interacting with the data source.
        """
        self.repository = repository

    def get_all_users(self):
        """
        Retrieves all users from the repository.

        This method fetches all user records from the data source using the repository's
        `get_all` method.

        Returns:
            list: A list of `User` objects representing all users in the data source.
        """
        return self.repository.get_all()

    def get_user(self, user_id):
        """
        Retrieves a single user by their ID.

        This method fetches a user record from the data source using the repository's
        `get_by_id` method.

        Args:
            user_id: The ID of the user to retrieve.

        Returns:
            User: A `User` object representing the user with the specified ID.

        Raises:
            UserNotFound: If the user with the given ID does not exist in the data source.
        """
        return self.repository.get_by_id(user_id)

    def create_user(self, name):
        """
        Creates a new user with the specified name.

        This method initializes a new `User` object with the provided name and adds
        it to the data source using the repository's `add` method.

        Args:
            name: The name of the user to create.

        Returns:
            User: The newly created `User` object with its ID assigned by the data source.
        """
        user = User(None, name)
        self.repository.add(user)
