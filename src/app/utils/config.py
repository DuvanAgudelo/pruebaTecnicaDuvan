import logging
import os


class Config:
    DEBUG = True
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DB = os.getenv("MYSQL_DB")

    @staticmethod
    def configure_logging():
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[logging.StreamHandler()],
        )


class DevelopmentConfig(Config):
    DEBUG = True
    HOST = "127.0.0.1"
    PORT = 5000


class ProductionConfig(Config):
    DEBUG = False
    HOST = "0.0.0.0"
    PORT = 5000


config = {"development": DevelopmentConfig, "production": ProductionConfig}
