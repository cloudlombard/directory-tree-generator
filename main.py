import argparse
import os

parser = argparse.ArgumentParser(description="Insert a folder path: ")
parser.add_argument("fpath", metavar="fpath", type=str, nargs="?",
                    help="a folder path to be processed by the directory tree generator")
args = parser.parse_args()

path = args.fpath
for dirpath, dirnames, filenames in os.walk(path):
    directory_level = dirpath.replace(path, "")
    directory_level = directory_level.count(os.sep)
    indent = " " * 4
    print("{}{}/".format(indent * directory_level, os.path.basename(dirpath)))
    for f in filenames:
        print("{}{}".format(indent * (directory_level + 1), f))
