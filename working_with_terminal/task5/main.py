import os
import subprocess


current_dir = os.getcwd()

print(f"Your current directory is {current_dir}")

script = '''cd C:/Users/Dell/Desktop'''
sr = '''ls'''

os.system("powershell -c '%s'" % script)
os.system("powershell -c '%s'" % sr)

