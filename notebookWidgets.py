import lightcurvesPlots
import numpy as np
from csvWithMeta import readCSV
from IPython.html.widgets import interact, FloatSliderWidget, fixed

filters = ['f105w', 'f140w', 'f160w', 'f814w']


def paramsFromFile(filter1, filter2, filter3, filename):
    params, filters_dict = readCSV(filter1, filter2, filter3, filename)

    plotParams = dict(
        z=FloatSliderWidget(min=0.15, max=2, step=0.01, value=params['z']),
        x0=FloatSliderWidget(min=0, max=1e-5, step=0.1*1e-5,
                             value=params['x0']),
        x1=FloatSliderWidget(min=-3, max=2, step=0.1, value=params['x1']),
        c=FloatSliderWidget(min=-0.4, max=0.4, step=0.01,
                            value=params['c']),
        hostebv_cc=FloatSliderWidget(min=-0.1, max=0.65, step=0.1,
                                     value=0),
        phase=FloatSliderWidget(min=-50, max=150, step=1, value=0),
        dates=fixed([filters_dict[filter1]['time'],
                    filters_dict[filter2]['time'],
                    filters_dict[filter3]['time']]),
        filters=fixed([filter1, filter2, filter3]),
        data_flux_filter1=fixed(filters_dict[filter1]['flux']),
        data_flux_filter1_err=fixed(filters_dict[filter1]['flux_error']),
        data_flux_filter2=fixed(filters_dict[filter2]['flux']),
        data_flux_filter2_err=fixed(filters_dict[filter2]['flux_error']),
        data_flux_filter3=fixed(filters_dict[filter3]['flux']),
        data_flux_filter3_err=fixed(filters_dict[filter3]['flux_error']))

    return plotParams


def paramsFromHand(filter1, filter2, filter3):
    plotParams = dict(
        z=FloatSliderWidget(min=0.15, max=2, step=0.01, value=1.00),
        x1=FloatSliderWidget(min=-3, max=2, step=0.1, value=1.),
        c=FloatSliderWidget(min=-0.4, max=0.4, step=0.01,
                            value=0),
        hostebv_cc=FloatSliderWidget(min=-0.1, max=0.65, step=0.1,
                                     value=0),
        phase=FloatSliderWidget(min=-50, max=150, step=1, value=0),
        dates=np.asarray([[0, 32], [0, 32], [0, 32]]),
        filters=fixed([filter1, filter2, filter3]),
        data_flux_filter1=fixed([0.0, 4.93]),
        data_flux_filter1_err=fixed([0.26, 0.23]),
        data_flux_filter2=fixed([0.0, 5.08]),
        data_flux_filter2_err=fixed([0.2, 0.2]),
        data_flux_filter3=fixed([0, 1.15]),
        data_flux_filter3_err=fixed([0.3, 0.3]))

    return plotParams


def createPlots(filter1, filter2, filter3, type, filename=None):
    if type == 'Ia':
        lightcurvesPlotsFunc = lightcurvesPlots.plot_Ia
    elif type == 'Ibc':
        lightcurvesPlotsFunc = lightcurvesPlots.plot_Ibc
    elif type == 'II':
        lightcurvesPlotsFunc = lightcurvesPlots.plot_II

    if filename is not None:
        p = paramsFromFile(filter1, filter2, filter3, filename)
    else:
        p = paramsFromHand(filter1, filter2, filter3)

    interact(lightcurvesPlotsFunc, **p)
