from astropy.io import ascii
filters = ['f105w', 'f140w', 'f160w', 'f814w']


def readCSV(filter1, filter2, filter3, filename):
    ''' Takes an sncosmo csv-like file, returns a dictionary with the metadata
    and a nested dictionary. The nested dictionary contains the flux, flux error
    , and time (MJD - MJD(0)) for each filter.
    '''
    my_data = ascii.read(filename, comment=r'\s*@')
    keys = []
    values = []
    for element in my_data.meta['comments']:
        key, value = element.split()
        keys.append(key)
        values.append(float(value))

    params = dict(zip(keys, values))
    t0 = params['t0']
    filters_dict = {f: {'time': [], 'flux': [], 'flux_error': []} for f in filters}
    for f in filters:
        indices = [i for i, x in enumerate(my_data['band']) if x == f]
        filters_dict[f]['time'] = [my_data['mjd'][i] - t0 for i in indices]
        filters_dict[f]['flux'] = [my_data['flux'][i] for i in indices]
        filters_dict[f]['flux_error'] = [my_data['fluxerr'][i] for i in indices]

    return params, filters_dict

if __name__ == '__main__':
    filename = 'test.csv'

    params, filters_dict = readCSV('f140w', 'f105w', 'f814w', filename)
    print(params)
    print(filters_dict)
