import pathlib
import os


STATIC_DIR = os.path.join(pathlib.Path(__file__).parent)

def get_file(fname) -> str:
    with open(os.path.join(STATIC_DIR, fname), "rt") as f:
        data = f.read()

    return data