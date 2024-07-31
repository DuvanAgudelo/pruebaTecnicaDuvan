from app.models import User
from app.utils.exceptions import UserNotFound


class UserRepository:
    """
    Repository class for managing user data in a MySQL database.

    This class provides methods to interact with the `users` table in the MySQL
    database, including retrieving all users, fetching a user by ID, and adding
    a new user.

    Attributes:
        mysql (MySQL): An instance of the `MySQL` class for connecting to the database.
    """

    def __init__(self, mysql):
        """
        Initializes the UserRepository with a MySQL connection instance.

        Args:
            mysql: An instance of the `MySQL` class used for database operations.
        """

        self.mysql = mysql

    def get_all(self):
        """
        Retrieves all users from the `users` table.

        Executes a SQL query to fetch all user records and returns a list of `User` objects.

        Returns:
            list: A list of `User` objects representing all users in the database.
        """

        query = "SELECT * FROM users"
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
        return [User(row[0], row[1], row[2]) for row in rows]

    def get_by_id(self, user_id):
        """
        Retrieves a user by their ID.

        Executes a SQL query to fetch a user record by ID.

        Args:
            user_id: The ID of the user to retrieve.

        Returns:
            User: A `User` object representing the user with the specified ID.

        Raises:
            UserNotFound: If no user with the given ID exists in the database.
        """

        query = "SELECT * FROM users WHERE id = %s"
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(query, (user_id,))
            row = cursor.fetchone()
            if row:
                return User(row[0], row[1], row[2])
            else:
                raise UserNotFound(user_id)

    def add(self, user):
        """
        Adds a new user to the `users` table.

        Executes a SQL query to insert a new user record.

        Args:
            user (User): The `User` object to add to the database.

        Returns:
            User: The `User` object with the ID and timestamp updated.
        """

        query = "INSERT INTO users (name, created_at) VALUES (%s, %s)"
        with self.mysql.connection.cursor() as cursor:
            cursor.execute(query, (user.name, user.created_at))
            self.mysql.connection.commit()
            user.id = cursor.lastrowid
        return user
