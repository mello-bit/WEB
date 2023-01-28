from zipfile import ZipFile
import os
from os.path import join


def human_read_format(size):
    sizes = ["Б", "КБ", "МБ", "ГБ"]
    save_i = 0
    for i in range(4):
        if size >= 1024:
            size = round(size / 1024)
        else:
            save_i = i
            break

    return f"{size}{sizes[save_i]}"


with ZipFile('input.zip') as myzip:

    for name in myzip.filelist:

        items = name.filename.rstrip("/").split("/")
        if "file_size" in str(name):
            print(
                f'{"  " * (len(items) - 1) + items[-1]} {human_read_format(name.file_size)}')
        else:
            print("  " * (len(items) - 1) + items[-1])


# with ZipFile('input.zip') as myzip:
#     r = myzip.filelist
#     for name in r:
#         print(name.filename, name.file_size)
#         print("file_size" in str(name))
#         print()

# print(os.listdir())
