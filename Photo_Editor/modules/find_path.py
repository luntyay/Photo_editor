import os

def find_path_file(filename):
    abs_path = __file__.split("\\")
    del abs_path[-1]
    del abs_path[-1]
    abs_path = '\\'.join(abs_path)
    abs_path = os.path.join(abs_path, filename)
    return abs_path

