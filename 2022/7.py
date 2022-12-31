# 1 Go line by line
# cd, ls the cd'd directory
# If directory: find dir in list and recursively call from 1
# If not directory: mark file size
from collections import defaultdict

dir_dict = defaultdict()
path = []


def add_dir(path, direc):

    path.append(direc)


def rm_dir(path):

    path = path[:-1]


def find_direc(data, direc):

    direc_cmd = f"$ cd {direc}"
    add_dir(path, direc)

    direc_index = data.index(direc_cmd)
    iter_data = iter(data[direc_index:])
    dir_dict[direc] = dict(contains=[], size=0)
    ls_complete = False
    while True:
        try:
            line = next(iter_data)
        except StopIteration:
            break
        if "$" in line:  # cd or ls  # ** Breaks too early if not all dirs contained within; check
            break
        if "dir" in line:
            # Mark dir as existing under this dir, then find the contents of that dir
            dir_dict[direc]['contains'].append(line[4:])
            find_direc(line[4:])
        else:
            # Get file size (later: get size of each dir)
            file_size = int(line.split(" ")[0])
            dir_dict[direc]['size'] += file_size


if __name__ == "__main__":

    with open('7_test.txt', 'r') as fo:
        data = fo.read().splitlines()
    find_direc(data=data, direc='/')
    print("Debug")