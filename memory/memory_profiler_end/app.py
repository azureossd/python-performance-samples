## Sample code taken from Official Library repository https://github.com/pythonprofilers/memory_profiler/blob/master/examples/numpy_example.py

import numpy as np
import scipy.signal
from memory_profiler import profile

@profile(precision=4)
def create_data():
    ret = []
    for n in range(50):
        ret.append(np.random.randn(1, 70, 71, 72))
    return ret
    
@profile(precision=4)
def process_data(data):
    data = np.concatenate(data)
    detrended = scipy.signal.detrend(data, axis=0)
    return detrended

if __name__ == "__main__":
    raw_data = create_data()
    processed_data = process_data(raw_data)