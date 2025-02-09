print(directory1)
print(directory2)

for directory in [directory1, directory2]:
    if not os.access(directory, os.F_OK):
        print(directory, "is not a valid directory!")
        sys.exit()

def md5(file_path):
    read_file = open(file_path, "rb")
    the_hash = hashlib.md5()
    for line in read_file.readlines():
        the_hash.update(line)
    return the_hash.hexdigest()

def directory_listing(directory_name):
    dir_file_list = {}
    dir_root = None
    dir_trim = 0
    for path, dirs, files in os.walk(directory_name):