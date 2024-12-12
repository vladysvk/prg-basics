import re

with open("files.txt") as file:
    for line in file:
        if re.search(r"^.+\.html$", line):
            print(line)