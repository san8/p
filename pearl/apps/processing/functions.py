"""
Helper fucntions for Quality control & Processing.
"""

from contextlib import contextmanager
from os import getcwd
from os import chdir


@contextmanager
def cd(path):
    """
    A simple context manager to change directory.
    """
    old_dir = getcwd()
    chdir(path)
    try: yield
    finally: chdir(old_dir)
 
