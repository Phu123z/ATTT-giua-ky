

def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()


def write_file(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)
