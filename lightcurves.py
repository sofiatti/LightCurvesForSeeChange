import numpy as np
import sncosmo

t0 = 0
hostr_v = 3.1
dust = sncosmo.CCM89Dust()

zero_point = {'f105w': 26.235, 'f140w': 26.437, 'f160w': 25.921,
              'f814w': 25.0985, 'zpsys': 'ab'}

'''
def filter2bandpass(filter_file):
    """Returns the sncosmo bandpass for an HST filter"""
    filter = np.loadtxt(filter_file)
    wavelength = filter[:, 0]
    transmission = filter[:, 1]
    band = sncosmo.Bandpass(wavelength, transmission, name=filter_file[: -4])
    sncosmo.registry.register(band, force=True)
    return

# Only have to use once
f105w_wfc3ir = filter2bandpass('f105w_wfc3ir.dat')
f140w_wfc3ir = filter2bandpass('f140w_wfc3ir.dat')
f814w_wfc3uvis = filter2bandpass('f814w_wfc3uvis.dat')
'''


def lightcurve_Ia(filter, z, x1, c, x0=None):
    """Given a filter and redshift z, generates the observed
    flux for SNe Type Ia"""
    alpha = 0.12
    beta = 3.
    mabs = -19.1 - alpha*x1 + beta*c
    zp = zero_point[filter]
    zpsys = zero_point['zpsys']

    # Checking if bandpass is outside spectral range for SALT2. If yes,
    # use salt2-extended.
    salt_name = 'salt2'
    salt_version = '2.4'

    rest_salt_max_wav = 9200
    rest_salt_min_wav = 2000

    salt_max_wav = (1 + z) * rest_salt_max_wav
    salt_min_wav = (1 + z) * rest_salt_min_wav

    band = sncosmo.get_bandpass(filter)
    if (band.wave[0] < salt_min_wav or band.wave[-1] > salt_max_wav):
        salt_name = 'salt2-extended'
        salt_version = '1.0'

    # Type Ia model
    model_Ia = sncosmo.Model(source=sncosmo.get_source(salt_name,
                                                       version=salt_version))
    if x0 is not None:
        p = {'z': z, 't0': t0, 'x0': x0, 'x1': x1,
             'c': c}
    else:
        p = {'z': z, 't0': t0, 'x1': x1, 'c': c}
        model_Ia.set(z=z)
        model_Ia.set_source_peakabsmag(mabs, 'bessellb', 'vega')
    model_Ia.set(**p)
    phase_array = np.linspace(model_Ia.mintime(), model_Ia.maxtime(), 100)
    obsflux_Ia = model_Ia.bandflux(filter, phase_array, zp=zp, zpsys=zpsys)
    keys = ['phase_array', 'obsflux']
    values = [phase_array, obsflux_Ia]
    dict_Ia = dict(zip(keys, values))
    np.savetxt('test.dat', np.c_[dict_Ia['phase_array'], dict_Ia['obsflux']])
    x0 = model_Ia.get('x0')
    return (dict_Ia, x0, salt_name, salt_version)


def lightcurve_Ibc(filter, z, hostebv_Ibc):
    """Given a filter, redshift z at given phase, generates the observed
    magnitude for SNe Type Ibc"""
    zp = zero_point[filter]
    zpsys = zero_point['zpsys']
    model_Ibc = ['s11-2005hl', 's11-2005hm', 's11-2006fo', 'nugent-sn1bc',
                 'nugent-hyper', 's11-2006jo', 'snana-2004fe',
                 'snana-2004gq', 'snana-sdss004012', 'snana-2006fo',
                 'snana-sdss014475', 'snana-2006lc', 'snana-04d1la',
                 'snana-04d4jv', 'snana-2004gv', 'snana-2006ep',
                 'snana-2007y', 'snana-2004ib', 'snana-2005hm',
                 'snana-2006jo', 'snana-2007nc']
    obsflux_Ibc = []
    phase_arrays = []
    for i in model_Ibc:
        model_i = sncosmo.Model(source=sncosmo.get_source(i), effects=[dust],
                                effect_names=['host'], effect_frames=['rest'])
        mabs = -17.56
        model_i.set(z=z)
        phase_array_i = np.linspace(model_i.mintime(), model_i.maxtime(), 100)
        model_i.set_source_peakabsmag(mabs, 'bessellb', 'ab')
        p_core_collapse = {'z': z, 't0': t0, 'hostebv': hostebv_Ibc,
                           'hostr_v': hostr_v}
        model_i.set(**p_core_collapse)
        phase_arrays.append(phase_array_i)
        obsflux_i = model_i.bandflux(filter, phase_array_i, zp, zpsys)
        obsflux_Ibc.append(obsflux_i)
    keys = model_Ibc
    values = []
    for i, item in enumerate(model_Ibc):
        values.append([obsflux_Ibc[i], phase_arrays[i]])
    dict_Ibc = dict(zip(keys, values))
    return (dict_Ibc)


def lightcurve_II(filter, z, hostebv_II):
    """Given a filter and redshift z, generates the observed magnitude for
    SNe Type II"""
    zp = zero_point[filter]
    zpsys = zero_point['zpsys']
    model_II = ['s11-2005lc', 's11-2005gi', 's11-2006jl', 'nugent-sn2p',
                'snana-2004hx', 'snana-2005gi', 'snana-2006gq',
                'snana-2006kn', 'snana-2006jl', 'snana-2006iw',
                'snana-2006kv', 'snana-2006ns', 'snana-2007iz',
                'snana-2007nr', 'snana-2007nr', 'snana-2007kw',
                'snana-2007ky', 'snana-2007lj', 'snana-2007lb',
                'snana-2007ll', 'snana-2007nw', 'snana-2007ld',
                'snana-2007md', 'snana-2007lz', 'snana-2007lx',
                'snana-2007og', 'snana-2007ny', 'snana-2007nv',
                'snana-2007pg', 's11-2004hx', 'nugent-sn2l', 'nugent-sn2n',
                'snana-2006ez', 'snana-2006ix']
    obsflux_II = []
    phase_arrays = []
    for i in model_II:
        model_i = sncosmo.Model(source=sncosmo.get_source(i), effects=[dust],
                                effect_names=['host'],
                                effect_frames=['rest'])
        if i == 's11-2004hx' == 'nugent-sn2l':
            mabs = -17.98
        else:
            mabs = -16.75
        model_i.set(z=z)
        phase_array_i = np.linspace(model_i.mintime(), model_i.maxtime(), 100)
        model_i.set_source_peakabsmag(mabs, 'bessellb', 'ab')
        p_core_collapse = {'z': z, 't0': t0, 'hostebv': hostebv_II,
                           'hostr_v': hostr_v}
        model_i.set(**p_core_collapse)
        phase_arrays.append(phase_array_i)
        obsflux_i = model_i.bandflux(filter, phase_array_i, zp, zpsys)
        obsflux_II.append(obsflux_i)
    keys = model_II
    values = []
    for i, item in enumerate(model_II):
        values.append([obsflux_II[i], phase_arrays[i]])
    dict_II = dict(zip(keys, values))
    return (dict_II)
