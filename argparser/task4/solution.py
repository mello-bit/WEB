import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--upper", action="store_true", dest="isUpper")
parser.add_argument("--lines", nargs='?', type=int)
# parser.add_argument("ln", type=int, nargs='?')
parser.add_argument("fileRd", type=str)
parser.add_argument("fileWr", type=str)

args = parser.parse_args()

with open(args.fileRd, "r", encoding="utf8") as file, open(args.fileWr, "w", encoding="utf8") as wFile:
    count = 0
    scr = []

    for line in file.readlines():
        # print(line.split('\\n'))
        for s in line.split("\\n"):
            scr.append(s.strip())
            break

    res = []
    if args.lines is not None:

        while count < args.lines and count < len(scr):
            if args.isUpper:
                res.append(scr[count].upper())
            else:
                res.append(scr[count])

            count += 1

    else:
        res = scr

    wFile.write('\n'.join(res))
