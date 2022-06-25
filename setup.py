from os import getenv, walk, path
from platform import system

read = []
with open("Game.spec", "rt", encoding="utf-8") as file:
    read = file.readlines()

for index, line in enumerate(read):
    if line.startswith("assets ="):
        newassets = []
        for (dirpath, dirnames, filenames) in walk("assets"):
            for dirname in dirnames:
                asset = (path.join(dirpath, dirname, "*"), path.join(dirpath, dirname))
                newassets.append(asset)
        read[index] = f"assets = {newassets}\n"
    if line.startswith("a = Analysis"):
        read[index+1] = f"    ['{path.join('src', 'Game.py')}'],\n"
    if line.startswith("    name="):
        version = getenv('VERSION')
        read[index] = f"    name='Mine-Mine-Mine-v{version}-{system()}',\n"

with open("Game.spec", "wt", encoding="utf-8") as file:
    file.writelines(read)
