import os
import pickle

def save_object(file_path, obj):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "wb") as file:
        pickle.dump(obj, file)
