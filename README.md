# User Greeter

This application allows you to persist users after saving them. It is developed in Python using the Flask framework. The application has three main routes that interact with a user database.

# Instructions to Run the Application

This application can be run in three different ways: locally, using Docker Compose, or in a Kubernetes cluster. The steps for each method are detailed below.

## Requirements

- Python 3.x
- Docker
- Minikube  (for local testing)

## Running Locally

To run the application locally, follow these steps:

1. **Create a Virtual Environment:**:

   Open a terminal and navigate to the project directory (FLASK). Then, execute the following commands to create a virtual environment:

   ```bash
   python -m venv venv
   .\venv\Scripts\Activate
   ```
  
2.  **Install Dependencies:**:

    Execute the command:

    ```bash
    pip install .
    ```
    This will install the necessary dependencies to run the application.

3. **Configure the Database:**:

    Ensure that a MySQL database is running on port 3306. Access the database with the following command:

    ```bash
    mysql -u root -p -h localhost
    ```

    Enter the password you assigned to the root user of the database. Then, execute the following SQL script to create the database and the necessary table:

    ```bash
    CREATE DATABASE IF NOT EXISTS flask_app;

    USE flask_app;

    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    ```

4. **Configure Environment Variables:**:

    Set the environment variables. On Windows, you can do this using PowerShell as follows:

    ```powershell
      $env:MYSQL_PORT = "<port number it is 3306 by defect >"
      $env:MYSQL_USER = "<user>"
      $env:MYSQL_PASSWORD = "<password>"
      $env:MYSQL_DB = "flask_app"
      $env:MYSQL_HOST = "<host>"
     ```
     For local testing, set the host as localhost.

5. **Run the Application**

    To run the application, execute the following command:

    ```bash
    user_greeting
    ```


6. **Application Usage**
    This application has three routes:

    1. **`/hello`**:  This route accepts a payload with a user name. This name can contain alphanumeric characters, accents, and diacritics, but does not accept special characters. It will persist the user with the name and a timestamp of when the user was created.

        - Method: POST
        - Example Curl:
          ```bash
            curl --location 'http://127.0.0.1:5000/hello' \
            --header 'Content-Type: application/json' \
            --data '{
                "name":"USER NAME"
            }'
          ```
        - Response: Returns a greeting with the user's name.

    2. **`/list`**: This route shows a list of all users in the database.

        - Method: POST
        - Example Curl:
          ```bash
            curl --location --request POST 'http://127.0.0.1:5000/list'
          ```
        - Example Response: 
          ```json
          [
            {
              "id": 1,
              "name": "test1",
              "created_at": "2024-07-27T07:19:21Z"
            },
            {
              "id": 2,
              "name": "test2",
              "created_at": "2024-07-27T08:20:21Z"
            }
          ]
          ```

    3. **`/user/<id>`**: This route shows the details of a specific user, where <id> is an integer representing the user ID.

        - Method: GET
        - Example Response for `/user/1`:
          ```json
          {
            "id": 1,
            "name": "Test1",
            "created_at": "2024-07-27T07:19:21Z"
          }
          ```

## Running with Docker

To run the application using Docker, follow these steps:

1. **Configure Environment Variables**

   Set the environment variables. On Windows, you can do this using PowerShell as follows:

      ```bash
      $env:MYSQL_DATABASE = "flask_app"
      $env:MYSQL_ROOT_PASSWORD = "<root user password>"
      $env:MYSQL_USER = "<for local testing, use root>"
      $env:MYSQL_PASSWORD = "<root user password>"
      ```
      

**Note:** In a production environment, such as with Kubernetes, a different user than root should be used. To modify the user for this use case, edit the init.sql file. This file contains the script to create the database and table, and add a new user. Also, update the environment variables accordingly. It is recommended to restrict the permissions to read and write for this user.

2. **Run Docker Compose**
   To run the application, execute the following command:

   ```bash
   docker-compose up --build
   ```
   This will build the application container.


3. **Application Usage**
    This application has three routes, as described here:

    1. **`/hello`**:  This route accepts a payload with a user name. This name can contain alphanumeric characters and accents. But does not accept special characters. It will persist the user with the name and a timestamp of when the user was created.
    
        - Method: POST
        - Example Curl:
          ```bash
            curl --location 'http://127.0.0.1:8080/hello' \
            --header 'Content-Type: application/json' \
            --data '{
                "name":"USER NAME"
            }'
          ```
        - Response: Returns a greeting with the provided name.

    2. **`/list`**: This route shows a list of all users in the database.

        - Method: POST
        - Example Curl:

          ```bash
            curl --location --request POST 'http://127.0.0.1:8080/list'
          ```
        - Example Response:

          ```json
          [
            {
              "id": 1,
              "name": "test1",
              "created_at": "2024-07-27T07:19:21Z"
            },
            {
              "id": 2,
              "name": "test2",
              "created_at": "2024-07-27T08:20:21Z"
            }
          ]
          ```

    3. **`/user/<id>`**:  This route shows the details of a specific user, where <id> is an integer representing the user ID.

        - Method: POST
        - Example Request:

          ```bash
          curl --location --request POST 'http://127.0.0.1:8080/user/1'
          ```
        - Example Response for `/user/1`:

          ```json
          {
            "id": 1,
            "name": "test1",
            "created_at": "2024-07-27T07:19:21Z"
          }
          ```

**Note:** In the Docker Compose file, a container with an Nginx proxy is set up to block GET requests. Additionally, it ensures that the ID in 'http://127.0.0.1:8080/user/id' is numeric and does not accept other values. If the request does not meet these criteria, a custom page will be displayed.

![CustomPage](/custom_page/customErrorPage.png)


## Running in Kubernetes

1. **Build Image**

   To ensure the Kubernetes deployment works, you first need to build the Docker image with this name "flask-web". Run the following command:
     ```bash
     docker build -t flask-web:latest .
     ```

   **Note:** If you are running Kubernetes locally with Minikube, the image might not be found locally. In that case, you can run the command:

   ```bash
    minikube image load flask-web:latest
   ```

2. **Start Minikube**

   Open a terminal and execute the following command to start Minikube:

   ```bash
   minikube start
   ```

3. **Deploy the Necessary Resources**

   Open a terminal and execute the following command to create the necessary resources in the Kubernetes cluster:

   ```bash
   cd kubernetes
   kubectl apply -f deployment.yml
   ```

4. **Create a Tunnel to the Nginx Service**

   This exposes the Nginx service outside the Kubernetes cluster, allowing interaction with the application. It provides a quick solution for local testing.

   ```bash
    minikube service nginx -n junior-test
   ```
  This command will give you a URL to point to for testing. The Nginx service is of type Node with port 3007.

   **Note:** A job is created in the deployment.yml file. This job creates a user to avoid connecting to the database using the root user.

   **Note about Secrets** In deployment.yml, a secret is created with values for local testing. To change these values, write the new value in base64.

## Unit Tests

To run unit tests, make sure you are in the Python environment and execute this command:

```bash
pytest
```

## Docker Image Vulnerability Tests

To test for vulnerabilities in the Docker image, you can run these commands, allowing you to see which dependencies need to be updated.

```bash
docker scout quickview flask-web:latest
docker scout cves flask-web:latest 
```
  
