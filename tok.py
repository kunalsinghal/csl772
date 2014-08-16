import sys

for line in sys.stdin:
    line = line.strip()
    print line
    print len(line.split())
    for x in line.split():
        print x
