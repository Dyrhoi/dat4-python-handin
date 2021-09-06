import argparse
from genericpath import isfile
import os
import pathlib

default_output_path = "resources/week2/output.txt"

def get_file_names(folderpath,out=default_output_path):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""

    files = [name for name in os.listdir(folderpath) if os.path.isfile(os.path.join(folderpath, name))];
    files_to_string = "\n".join(files)
    write_to_file(out, files_to_string)
    return files

def get_all_file_names(folderpath,out=default_output_path):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""

    lst = []
    for path, subdirs,  files in os.walk(folderpath):
        for name in files:
            lst.append(str(pathlib.PurePath(path, name)))
    
    write_to_file(out, "\n".join(lst))

def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""

    lines = []
    for file in file_names:
        if os.path.isfile(file): 
            with open(file) as file:
                lines.append(file.readline().rstrip())
    print(lines)

def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""

    lines = []
    for file in file_names:
        if os.path.isfile(file): 
            with open(file) as file:
                for line in file:
                    if "@" in line:
                        lines.append(line.rstrip())
    print(lines)

def write_headlines(md_files, out=default_output_path):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""

    lines = []
    for file in md_files:
        if os.path.isfile(file): 
            with open(file) as file:
                for line in file:
                    if line.startswith("#"):
                        lines.append(line.rstrip())
    write_to_file(out, "\n".join(lines))


def read_csv(csv_file):
    try:
        with open(csv_file) as file:
            return file.read()
    except EnvironmentError:
        print(csv_file + " was not found on system.")

def write_to_file(file, content):
    try:
        with open(file, "w") as file:
            file.write(content)
            print("Successfully wrote to file, " + file.name)
    except EnvironmentError:
        print(file + " was not found on system.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="List content of folder or csv",
    )

    parser.add_argument("path", type=str, help="path of csv file")
    parser.add_argument("--file", dest="output", type=str, help="optional filename of file to copy contents to")

    args = parser.parse_args()

    csv = read_csv(args.path)

    if args.output:
        write_to_file(args.output, csv)
    else:
        print(csv)