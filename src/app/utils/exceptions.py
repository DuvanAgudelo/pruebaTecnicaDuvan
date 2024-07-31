class InvalidDataError(Exception):
    """
    Exception raised for errors in the input data.
    """

    def __init__(self, message="Invalid data provided."):
        self.message = message
        super().__init__(self.message)


class UserNotFound(Exception):
    """
    Exception raised when a user is not found.
    """

    def __init__(self, user_id, message="User with id: {user_id} does not exist"):
        self.message = message.format(user_id=user_id)
        super().__init__(self.message)
