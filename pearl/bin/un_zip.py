"""
Helper fucntions for Quality control & Processing.
"""

from os import listdir, devnull, getcwd, chdir 
from subprocess import call
from contextlib import contextmanager


@contextmanager
def cd(path):
    """
    A simple context manage to change directory.
    """
    old_dir = getcwd()
    chdir(path)
    try: yield
    finally: chdir(old_dir)



def unzip_files(path):
    """
    Unzip the files in the given location & remove zip files.
    """
    zip_files = [files for files in listdir(path)]
    with cd(path):
        for zip_file in zip_files:
            commands = [["7z", "e", zip_file], ["rm", zip_file]]
            for command in commands:
                call(command, stdout=open(devnull, 'wb'))


loc = "/home/k3/work/pearl_project/pearl/media/NewProject/227"
unzip_files(loc)

