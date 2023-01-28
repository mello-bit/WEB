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


print(human_read_format(15000))