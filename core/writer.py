import csv
import os


class CSVWriter:
    keys = ('first_name', 'last_name', 'country', 'city', 'bdate', 'sex')

    def __init__(self):
        filepath = f'{os.getenv("FPATH")}.{os.getenv("FORMAT")}'
        f = open(filepath, 'w')
        self.writer = csv.writer(f)
        self.writer.writerow(CSVWriter.keys)

    @staticmethod
    def prepare_row(friend):
        row = []
        for key in CSVWriter.keys:
            info = friend.get(key)
            if (key == 'country' or key == 'city') and info:
                info = friend[key]['title']

            if key == 'bdate' and info:
                bdate = info.split('.')
                bdate.reverse()
                info = ".".join(bdate)

            if key == 'sex' and info:
                info = 'm' if friend[key] == 2 else 'f'

            row.append(info)
        return row

    def write(self, friend):
        row = self.prepare_row(friend)
        self.writer.writerow(row)
