import os


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


def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total


path = input("Please enter the path: ").replace('\\', '/')

files = os.listdir(path)
os.chdir(path)
for_delete = []
count = 0
for file in files:
    if count >= 10:
        break
    if os.path.isfile(file):
        for_delete.append([file, os.stat(file).st_size])
        # print(file, human_read_format(os.stat(file).st_size))
    else:
        for_delete.append([file, get_dir_size(file)])
        # print(file, human_read_format(get_dir_size(file)))

    count += 1


for f in sorted(for_delete, key=lambda f: f[1], reverse=True):
    print(f[0], human_read_format(f[1]))
