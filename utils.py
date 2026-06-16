import os

def read_file(path):
    file = open(path, "r")
    content = file.read()
    return content


def get_environment():
    return os.environ
