import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import numpy as np

from lightcurves import lightcurve_Ia, lightcurve_Ibc, lightcurve_II


def plot_Ia(z, x1, c, filters, dates, data_flux_filter1, data_flux_filter1_err,
            data_flux_filter2, data_flux_filter2_err,
            data_flux_filter3, data_flux_filter3_err, phase, x0=None):

    all_phase0 = np.asarray(dates[0]) + phase*(1+z)
    all_phase1 = np.asarray(dates[1]) + phase*(1+z)
    all_phase2 = np.asarray(dates[2]) + phase*(1+z)

    plt.figure(figsize=(3, 9))
    gs1 = gridspec.GridSpec(3, 9)
    gs1.update(wspace=0.025, hspace=0.05)
    ax1 = plt.subplot2grid((3, 3), (0, 0))
    ax2 = plt.subplot2grid((3, 3), (0, 1))
    ax3 = plt.subplot2grid((3, 3), (0, 2))

    lightcurve_00, x0_0, salt_name_0, salt_version_0 = lightcurve_Ia(
        filters[0], z, x1, c, x0=x0)
    lightcurve_10, x0_1, salt_name_1, salt_version_1 = lightcurve_Ia(
        filters[1], z, x1, c, x0=x0)
    lightcurve_20, x0_2, salt_name_2, salt_version_2 = lightcurve_Ia(
        filters[2], z, x1, c, x0=x0)

    ax1.plot(lightcurve_00['phase_array'], lightcurve_00['obsflux'])
    ax1.errorbar(all_phase0, data_flux_filter1, xerr=0,
                 yerr=data_flux_filter1_err, fmt='o', c='k')
    ax1.set_ylabel('Flux (counts/s)', size=14)
    ax1_title = filters[0].upper()
    ax1.set_title(ax1_title, size=14)
    ax1.annotate('Type Ia', xy=(0.75, 0.85), xycoords='axes fraction', size=14)
    ax1.annotate('z=%.2f' % z, xy=(0.75, 0.75), xycoords='axes fraction',
                 size=14)
    ax1.annotate('x0=%.1E' % x0_0, xy=(0.65, 0.65), xycoords='axes fraction',
                 size=14)
    ax1.annotate(salt_name_0 + '-' + salt_version_0, xy=(0.05, 0.85),
                 xycoords='axes fraction', size=14)

    ax2.plot(lightcurve_10['phase_array'], lightcurve_10['obsflux'])
    ax2.errorbar(all_phase1, data_flux_filter2, xerr=0,
                 yerr=data_flux_filter2_err, fmt='o', c='k')
    ax2_title = filters[1].upper()
    ax2.set_title(ax2_title, size=14)
    ax2.annotate('Type Ia', xy=(0.75, 0.85), xycoords='axes fraction', size=14)
    ax2.annotate('z=%.2f' % z, xy=(0.75, 0.75), xycoords='axes fraction',
                 size=14)
    ax2.annotate('x0=%.1E' % x0_1, xy=(0.65, 0.65), xycoords='axes fraction',
                 size=14)
    ax2.annotate(salt_name_1 + '-' + salt_version_1, xy=(0.05, 0.85),
                 xycoords='axes fraction', size=14)

    ax3.plot(lightcurve_20['phase_array'], lightcurve_20['obsflux'])
    ax3.errorbar(all_phase2, data_flux_filter3, xerr=0,
                 yerr=data_flux_filter3_err, fmt='o', c='k')
    ax3_title = filters[2].upper()
    ax3.set_title(ax3_title, size=14)
    ax3.annotate('Type Ia', xy=(0.75, 0.85), xycoords='axes fraction', size=14)
    ax3.annotate('z=%.2f' % z, xy=(0.75, 0.75), xycoords='axes fraction',
                 size=14)
    ax3.annotate('x0=%.1E' % x0_2, xy=(0.65, 0.65), xycoords='axes fraction',
                 size=14)
    ax3.annotate(salt_name_2 + '-' + salt_version_2, xy=(0.05, 0.85),
                 xycoords='axes fraction', size=14)

    fig = plt.gcf()
    fig.set_size_inches(18.5, 12.5)


def plot_Ibc(z, hostebv_cc, filters, dates,
             data_flux_filter1, data_flux_filter1_err,
             data_flux_filter2, data_flux_filter2_err,
             data_flux_filter3, data_flux_filter3_err, phase):
    model_Ibc = ['s11-2005hl', 's11-2005hm', 's11-2006fo', 'nugent-sn1bc',
                 'nugent-hyper', 's11-2006jo', 'snana-2004fe',
                 'snana-2004gq', 'snana-sdss004012', 'snana-2006fo',
                 'snana-sdss014475', 'snana-2006lc', 'snana-04d1la',
                 'snana-04d4jv', 'snana-2004gv', 'snana-2006ep',
                 'snana-2007y', 'snana-2004ib', 'snana-2005hm',
                 'snana-2006jo', 'snana-2007nc']

    all_phase0 = (dates[0] - dates[0][0]) + phase*(1+z)
    all_phase1 = (dates[1] - dates[1][0]) + phase*(1+z)
    all_phase2 = (dates[2] - dates[2][0]) + phase*(1+z)
    plt.figure(figsize=(3, 9))
    gs1 = gridspec.GridSpec(3, 9)
    gs1.update(wspace=0.025, hspace=0.05)
    ax1 = plt.subplot2grid((3, 3), (0, 0))
    ax2 = plt.subplot2grid((3, 3), (0, 1))
    ax3 = plt.subplot2grid((3, 3), (0, 2))

    lightcurve_00 = lightcurve_Ibc('f140w', z, hostebv_cc)
    lightcurve_10 = lightcurve_Ibc('f105w', z, hostebv_cc)
    lightcurve_20 = lightcurve_Ibc('f814w', z, hostebv_cc)

    for i in range(len(model_Ibc)):
        ax1.plot(lightcurve_00[model_Ibc[i]][1], lightcurve_00[model_Ibc[i]][0])
        ax1.errorbar(all_phase0, data_flux_filter1, xerr=0,
                     yerr=data_flux_filter1_err, fmt='o', c='k')

    ax1.set_ylabel('Flux (counts/s)', size=14)
    ax1.set_title('F140W', size=14)
    ax1.annotate('Type Ibc', xy=(0.75, 0.85), xycoords='axes fraction', size=14)
    ax1.annotate('z=%.2f' % z, xy=(0.75, 0.75), xycoords='axes fraction',
                 size=14)

    for i in range(len(model_Ibc)):
        ax2.plot(lightcurve_10[model_Ibc[i]][1], lightcurve_10[model_Ibc[i]][0])
        ax2.errorbar(all_phase1, data_flux_filter2, xerr=0,
                     yerr=data_flux_filter2_err, fmt='o',
                     c='k')
    ax2.set_title('F105W', size=14)
    ax2.annotate('Type Ibc', xy=(0.75, 0.85), xycoords='axes fraction', size=14)
    ax2.annotate('z=%.2f' % z, xy=(0.75, 0.75), xycoords='axes fraction',
                 size=14)

    for i in range(len(model_Ibc)):
        ax3.plot(lightcurve_20[model_Ibc[i]][1], lightcurve_20[model_Ibc[i]][0])
        ax3.errorbar(all_phase2, data_flux_filter3, xerr=0,
                     yerr=data_flux_filter3_err, fmt='o',
                     c='k')
    ax3.set_title('F814.UVIS', size=14)
    ax3.annotate('Type Ibc', xy=(0.75, 0.85), xycoords='axes fraction', size=14)
    ax3.annotate('z=%.2f' % z, xy=(0.75, 0.75), xycoords='axes fraction',
                 size=14)

    fig = plt.gcf()
    fig.set_size_inches(18.5, 12.5)


def plot_II(z, hostebv_cc, filters, dates, data_flux_filter1,
            data_flux_filter1_err, data_flux_filter2, data_flux_filter2_err,
            data_flux_filter3, data_flux_filter3_err, phase):
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

    all_phase0 = (dates[0] - dates[0][0]) + phase*(1+z)
    all_phase1 = (dates[1] - dates[1][0]) + phase*(1+z)
    all_phase2 = (dates[2] - dates[2][0]) + phase*(1+z)

    plt.figure(figsize=(3, 9))
    gs1 = gridspec.GridSpec(3, 9)
    gs1.update(wspace=0.025, hspace=0.05)
    ax1 = plt.subplot2grid((3, 3), (0, 0))
    ax2 = plt.subplot2grid((3, 3), (0, 1))
    ax3 = plt.subplot2grid((3, 3), (0, 2))

    lightcurve_00 = lightcurve_II('f140w', z, hostebv_cc)
    lightcurve_10 = lightcurve_II('f105w', z, hostebv_cc)
    lightcurve_20 = lightcurve_II('f814w', z, hostebv_cc)

    for i in range(len(model_II)):
        ax1.plot(lightcurve_00[model_II[i]][1], lightcurve_00[model_II[i]][0]),
        ax1.errorbar(all_phase0, data_flux_filter1, xerr=0,
                     yerr=data_flux_filter1_err, fmt='o', c='k')

    ax1.set_ylabel('Flux (counts/s)', size=14)
    ax1.set_title('F140W', size=14)
    ax1.annotate('Type II', xy=(0.75, 0.85), xycoords='axes fraction', size=14)
    ax1.annotate('z=%.2f' % z, xy=(0.75, 0.75), xycoords='axes fraction',
                 size=14)

    for i in range(len(model_II)):
        ax2.plot(lightcurve_10[model_II[i]][1], lightcurve_10[model_II[i]][0])
        ax2.errorbar(all_phase1, data_flux_filter2, xerr=0,
                     yerr=data_flux_filter2_err, fmt='o',
                     c='k')
    ax2.set_title('F105W', size=14)
    ax2.annotate('Type II', xy=(0.75, 0.85), xycoords='axes fraction', size=14)
    ax2.annotate('z=%.2f' % z, xy=(0.75, 0.75), xycoords='axes fraction',
                 size=14)

    for i in range(len(model_II)):
        ax3.plot(lightcurve_20[model_II[i]][1], lightcurve_20[model_II[i]][0])
        ax3.errorbar(all_phase2, data_flux_filter3, xerr=0,
                     yerr=data_flux_filter3_err, fmt='o',
                     c='k')
    ax3.set_title('F184W.UVIS', size=14)
    ax3.annotate('Type II', xy=(0.75, 0.85), xycoords='axes fraction', size=14)
    ax3.annotate('z=%.2f' % z, xy=(0.75, 0.75), xycoords='axes fraction',
                 size=14)

    fig = plt.gcf()
    fig.set_size_inches(18.5, 12.5)
