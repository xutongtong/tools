import re

def readText(path):
    mobiles = []
    with open(path) as f:
        for line in f.readlines():
            matches = re.search('(1\d{10})', line)
            if matches != None:
                mobile = matches.group(0)
                mobiles.append(mobile)
            else:
                print line + '\n'

    return mobiles


def writeText(origin_path, source_path):
    mobiles = readText(origin_path)

    with open(source_path, 'w') as f:
        for mobile in mobiles:
            f.write(mobile + '\n')


origin_path = '/tools/python/11.txt'
source_path = '/tools/python/12.txt'

writeText(origin_path, source_path)