import pickle
from pathlib import Path
_data = {}
def load(path: str):
    global _data
    if Path(path).is_file():
        with open(path, "rb") as f:
            _data = pickle.load(f)

def save(path: str):
    with open(path, "wb") as f:
        pickle.dump(_data, f)

def set(key, value):
    global _data
    _data[key] = value

def get(key):
    return _data[key]

