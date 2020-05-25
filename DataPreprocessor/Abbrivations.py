import csv


def lookup(abb):
    abb = abb.replace(".", "/")
    with open('../Dataset/Abbrivations.csv', encoding='utf-16') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if (abb == str(row[0])):
                return str(row[1])
        return 0


def add_abbrivation( abb, word):
    with open("../Dataset/abbrivations.csv", "a", newline="\n")as csv_file:
        line_writer = csv.writer(csv_file)
        line_writer.writerow([abb, word])
