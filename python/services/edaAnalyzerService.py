from numpy import arctan, degrees, mean
from scipy.signal import butter, filtfilt

class EdaAnalyzerService:

    TAG = __name__
    cutoff = 0.05
    order = 3


    def get_filter_params(self, fs: float, btype: str = 'lowpass'):
        return butter(self.order, 2*self.cutoff / fs, btype = btype)

    def filter(self, sig: list[float], fs: float):
        [b,a] = self.get_filter_params(fs)
        return filtfilt(b, a, sig, axis=0)

    def compute_derivative(self, sig: list[float], fs: float):
        lp = self.filter(sig, fs)
        ds = [s - lp[0] for s in lp[1:]]
        dt = [1/fs * i for i in range(1, len(ds)+1)]
        ds_dt = [x / t for x, t in zip(ds, dt)]
        angle = degrees(arctan(ds_dt))
        return mean(angle)

