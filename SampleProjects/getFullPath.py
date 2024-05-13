import os
import pathlib

# path of the given file
print(pathlib.Path("src/data.txt").parent.absolute())

# current working directory
print(pathlib.Path().absolute())

# path of the given file
print(os.path.dirname(os.path.abspath("src/data.txt")))

# current working directory
print(os.path.abspath(os.getcwd()))