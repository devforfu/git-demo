import csv
from collections import defaultdict


def read_file(fname):
    f = open(fname, 'r')
    reader = csv.DictReader(f, fieldnames=['product', 'cost'])
    _ = next(reader)
    products = defaultdict(lambda: 0)
    for row in reader:
        products[row['product'].strip()] += float(row['cost'])
    for name, price in products.items():
        print(f'{name} total price: {price:2.2f}')
    f.close()


def main():
    read_file('data.csv')


if __name__ == '__main__':
    main()
