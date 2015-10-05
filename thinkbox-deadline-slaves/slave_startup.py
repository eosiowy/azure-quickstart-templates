import subprocess
import sys
import re

AZURE_DATA_PATH = 'C:\\AzureData\\CustomData.bin'
DEADLINE_INI = 'C:\\ProgramData\\Thinkbox\\Deadline7\\deadline.ini'

def change_line(src, pattern, sub, dest=None, verbose=False):
    dest = dest if dest else src
    lines = []

    if verbose:
        print 'Editing:', src
        print 'Searching for:', pattern
        print 'Replacing with:', sub

    with open(src, 'r') as f:
        lines = f.readlines()

    with open(dest, 'w') as f:
        for line in lines:
            if verbose and re.search(pattern, line):
                print '\tBefore:', line
                print '\tAfter:', re.sub(pattern, sub, line)
            f.write(re.sub(pattern, sub, line))

def get_repo_path():
    with open(AZURE_DATA_PATH, 'r') as f:
        lines = f.readlines()

    if lines:
        return lines[0].strip()
    else:
        print 'ERROR: Repository IP not found.'
        sys.exit(1)

def main(argv):
    repo_path = get_repo_path()
    path_pattern = 'NetworkRoot=.*'
    new_path = r'NetworkRoot=' + repo_path.encode('string-escape')

    change_line(DEADLINE_INI, path_pattern, new_path, verbose=True)


if __name__ == '__main__':
    main(sys.argv[1:])
