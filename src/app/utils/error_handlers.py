from flask import jsonify
import logging
from app.utils.exceptions import UserNotFound, InvalidDataError


def register_error_handlers(app):
    """
    Registers custom error handlers for the Flask application.

    This function sets up custom error handlers for different types of exceptions
    that may occur during the application's runtime. It handles specific exceptions
    like UserNotFound and InvalidDataError, as well as a general exception handler
    for any other unexpected errors.
    """

    @app.errorhandler(UserNotFound)
    def handle_user_not_found(error):
        """
        Handle InvalidDataError exception.

        This function logs the InvalidDataError and returns a JSON response
        with the error message and a 400 status code.

        Returns:
            Response: JSON response with the error message and HTTP status 400.
        """

        logging.error(f"UserNotFound: {error}")
        response = jsonify({"error": str(error)})
        response.status_code = 404
        return response

    @app.errorhandler(InvalidDataError)
    def handle_invalid_data_error(error):
        """
        Handle InvalidDataError exception.

        This function logs the InvalidDataError and returns a JSON response
        with the error message and a 400 status code.

        Returns:
            Response: JSON response with the error message and HTTP status 400.
        """

        logging.error(f"InvalidDataError: {error}")
        response = jsonify({"error": str(error)})
        response.status_code = 400
        return response

    @app.errorhandler(Exception)
    def handle_general_error(error):
        """
        Handle general exceptions.

        This function logs any general exception and returns a JSON response
        with a generic error message and a 500 status code.

        Returns:
            Response: JSON response with a generic error message and HTTP status 500.
        """

        logging.error(f"Exception: {error}")
        response = jsonify({"error": "An unexpected error occurred"})
        response.status_code = 500
        return response
