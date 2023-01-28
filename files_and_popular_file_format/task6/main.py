from zipfile import ZipFile
import json


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


count = 0
with ZipFile('input.zip') as myzip:

    for name in myzip.filelist:

        items = name.filename.rstrip("/").split("/")
        if "file_size" in str(name) and items[-1].endswith(".json"):
            # print(name.filename)
            src = json.loads(myzip.read(name))
            # print(src)
            if src["city"] == "Москва":
                count += 1

print(count)
