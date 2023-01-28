from zipfile import ZipFile

with ZipFile('input.zip') as myzip:
    for name in myzip.namelist():
        items = name.rstrip("/").split("/")
        print("  " * (len(items) - 1) + items[-1])
