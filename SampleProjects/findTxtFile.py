import glob, os

os.chdir("src")

for file in glob.glob("*.txt"):
    print(file)