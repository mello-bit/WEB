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


def get_files_sizes():
    str_builder = []
    for i in os.listdir():
        if os.path.isfile(i):
            str_builder.append(f"{i} {human_read_format(os.path.getsize(i))}")

    return "\n".join(str_builder)


print(get_files_sizes())
