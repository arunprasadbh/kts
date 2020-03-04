from pathlib import Path
import sys

source_dir = Path('/Users/arunabhamidipati/ArunProjects/python/KTS')

files = source_dir.glob('*.csv')

dict1 = {"a":"1", "b":"2"}

print(dict1['a'])

for file_name in files:
    print(file_name)
    with open(file_name) as fp:
        for line in fp:
            print(line)
    print("***********")

