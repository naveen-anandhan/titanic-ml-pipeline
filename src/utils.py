import os
import pickle
import sys

from src.logger import logger
from src.exception import CustomException


def save_object(file_path, obj):
    try:
        logger.info(f"Saving object to {file_path}")

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "wb") as file:
            pickle.dump(obj, file)

        logger.info("Object saved successfully")

    except Exception as e:
        logger.error("Error while saving object")
        raise CustomException(e, sys)
