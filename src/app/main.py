from flask import Flask, request, jsonify
from app.utils.config import config
from app.utils.error_handlers import register_error_handlers
from flask_mysqldb import MySQL
from app.repository import UserRepository
from app.services import UserService
import logging


def create_app():
    app = Flask(__name__)
    app.config.from_object(config["development"])

    # Initialize MySQL connection
    connection = MySQL(app)

    # Create repository and service instances
    repository = UserRepository(connection)
    service = UserService(repository)

    # Register error handlers
    register_error_handlers(app)

    @app.route("/list", methods=["POST"])
    def get_users():
        """
        Fetch all users.

        Retrieves all users from the database using the UserService.
        It returns a JSON with a list of users.

        Returns:
            Response: JSON response with the list of users and HTTP status 200.
        """

        users = service.get_all_users()
        return jsonify([user.to_json() for user in users]), 200

    @app.route("/user/<int:id>", methods=["POST"])
    def get_user(id):
        """
        Fetch a user by ID.

        Retrieves a user by their ID using the UserService.
        Returns a JSON response containing the user data.

        Args:
            id: The unique identifier of the user.

        Returns:
            Response: JSON response with the user data and HTTP status 200.
        """

        logging.info(f"Fetching user with ID: {id}")
        user = service.get_user(id)
        return jsonify(user.to_json())

    @app.route("/hello", methods=["POST"])
    def create_user():
        """
        Create a new user.

        Creates a new user with the provided name using the UserService.
        It returns a JSON response with a greeting message.

        Request Body:
            name: The name of the new user.

        Returns:
            Response: JSON response with a greeting message
            and HTTP status 201.
        """
        data = request.get_json()
        name = data.get("name")
        service.create_user(name)
        return jsonify({"message": f"Hello {name}"}), 201

    return app


def main():
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
