import csv
import functools


def csv_format(func):
    @functools.wraps(func)
    def wrapped(*args):
        with open("log.scv", 'w') as file:
            writer = csv.writer(file)
            for line in args:
                writer.writerow(args)
        return func
    return wrapped


