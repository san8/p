import os
from os import chdir

from os.path import join, isfile


path = os.getcwd()
loc = os.path.join(path, 'bin')
files = [f for f in listdir(loc)]
print files
