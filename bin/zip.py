import os
from os import chdir

from os.path import join, isfile

@contextmanager
def cd(path):
    """
    A simple context manage to change directory.
    """
    old_dir = getcwd()
    chdir(path)
    try: yield
    finally: chdir(old_dir)
    ""
