import csv
import re
import glob

def readFiles(path, fileExt):
    return glob.glob(path + "/*." + fileExt)

def readCSV(filename, column=0, strip_str="\t"):
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        columns = [row[column].strip(strip_str) for row in reader]

    return columns

def writeText(contents, source_path):
    with open(source_path, 'w') as f:
        for content in contents:
            f.write(content + '\n')

def readText(path):
    contents = []
    with open(path) as f:
        for line in f.readlines():
            matches = re.search('(1\d{10})', line)
            if matches != None:
                content = matches.group(0)
                contents.append(content)
            else:
                print line + '\n'

    return contents

def reWriteText(origin_path, source_path):
    contents = readText(origin_path)

    with open(source_path, 'w') as f:
        for content in contents:
            f.write(content + '\n')


# path = "./csv"
# fileExt = "csv"
# csvs = readFiles(path, fileExt)
# mobile_column = 9
# mobiles = []

# print readCSV('./csv/1-1.csv', mobile_column)

# step-1 read csv
# for c in csvs:
#     # print c
#     # print readCSV(c, mobile_column)
#     mobiles = mobiles + (readCSV(c, mobile_column))
#
# mobiles_unique = set(mobiles)
# mobiles = list(mobiles_unique)
# print mobiles
# step-1 read csv
# filename = "1.csv"
# mobile_column = 9
# mobiles = readCSV(filename, mobile_column)
#
# step-2 write text
# txt_name = "1.txt"
# writeText(mobiles, txt_name)
#
# # step-3 rewrite text
# txt_name_2 = "1.new.txt"
# reWriteText(txt_name, txt_name_2)
# print len(column)

# step-4 read origin.csv
origin_csv = "origin.csv"
origin_mobiles = readCSV("origin.csv", 2)

txt_name = "origin.txt"
writeText(origin_mobiles, txt_name)

# step-3 rewrite text
txt_name_2 = "origin.new.txt"
reWriteText(txt_name, txt_name_2)
