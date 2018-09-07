import os

def makeDirectoryIfNotExist(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
