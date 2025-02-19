from pulse_lib.scan.read_input import read_channels


#this starts data collection and return the dataset.
def resonator_frequency_scan(sensor = 'S_East', f_range = 20e6):
    """
    Scan the resonator frequency of a sensor
    Args:
        sensor: which sensor to scan
        f_range: range to scan around the sensor frequency
    Returns:

    """
    sensor_freqs = {
        'S_North': 72.8e6,  # n
        'S_East': 86.4e6,  # e
        'S_West': 131.3e6,  # w
        'S_South': 170.3e6,  # s
    }

    rf_frequency = pulse.rf_params[sensor].frequency

    meas_param = read_channels(pulselib=pulse,
                            t_measure = 1e6,
                            channels = [sensor],
                            iq_mode = 'amplitude'
                            )

    f_center = sensor_freqs[sensor]
    f_min = f_center - f_range/2
    f_max = f_center + f_range/2

    dat = do1D(rf_frequency, f_min, f_max, 101, 0, meas_param,
            name='resonator_scan', reset_param = True).run()
  
    return dat #this dataset in in xarray format (https://docs.xarray.dev/en/stable/index.html)

def set_resonator_frequency(sensor, resonator_frequency):
    """
    Set the resonator frequency of a sensor
    Args:
        sensor: which sensor to scan
        resonator_frequency: frequency to set the sensor to
    Returns:

    """
    pulse.digitizer_channels[sensor].frequency = resonator_frequency
    return True


