from zipfile import ZipFile
import datetime
import shutil
import os


def make_reserve_arc(source: str, dest: str) -> None:
    time = str(datetime.datetime.now())
    time = time.split('.')[0].replace(' ', '_').replace(':', ';')

    name_of_dir = source.strip().replace('\\', '/').split('/')[-1]
    name_of_dir = name_of_dir.split('/')[-1]

    shutil.make_archive(name_of_dir + time, 'zip', root_dir=source)
    shutil.move(os.getcwd() + "\\" + name_of_dir + time + '.zip', dest)


make_reserve_arc(input(), input())
