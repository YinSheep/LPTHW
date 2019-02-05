# Practice for ex17
# Unnecessary direction and features are removed

from sys import argv
from os.path import exists

script, from_file, to_file = argv

out_file =open(to_file, 'w').write(open(from_file).read())

out_file.close()
