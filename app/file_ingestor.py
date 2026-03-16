import time

def tail_log(file_path):

    with open(file_path, "r") as f:

        f.seek(0,2)

        while True:

            line = f.readline()

            if not line:
                time.sleep(1)
                continue

            yield line.strip()