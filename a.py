import sys

for line in sys.stdin:
    print line
    for x in line.split():
        print x
