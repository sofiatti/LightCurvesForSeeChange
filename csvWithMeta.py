"""
csvWithMeta.py
"""

from astropy.io import ascii


def readCSV(file):
    my_data = ascii.read(file, comment=r'\s*@')
    keys = []
    values = []
    for element in my_data.meta['comments']:
        key, value = element.split()
        keys.append(key)
        values.append(float(value))

    params = dict(zip(keys, values))

    return params, my_data

if __name__ == '__main__':
    filename = 'test.csv'

    p, d = readCSV(filename)
    print(p)
    print(d)
